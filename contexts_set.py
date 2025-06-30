import streamlit as st
from PIL import Image
import requests
import os
from dotenv import load_dotenv
import base64
from gradio_client import Client, handle_file

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "compound-beta"

# Hugging Face captioning model (JoyCaption)
def generate_caption(image_path):
    client = Client("fancyfeast/joy-caption-beta-one")
    result = client.predict(
        input_image=handle_file(image_path),
        prompt="Write a long detailed description for this image.",
        temperature=0.6,
        top_p=0.9,
        max_new_tokens=512,
        log_prompt=True,
        api_name="/chat_joycaption"
    )
    return result

# Hugging Face VQA model (Sa2VA)
def answer_with_sa2va(image_path, question):
    client = Client("fffiloni/Sa2VA-simple-demo")
    result = client.predict(
        image_input_path=handle_file(image_path),
        prompt=question,
        api_name="/image_vision"
    )
    return result[0]  # Only the textual response

# Groq API with full context
def answer_with_groq(caption, vqa_answer, user_question):
    history = [{"role": "system", "content": f"You are a helpful multimodal assistant.\n\nCaption: {caption}"}]
    history += st.session_state.messages
    history.append({"role": "user", "content": user_question})

    payload = {
        "model": GROQ_MODEL,
        "messages": history,
        "temperature": 0.7,
        "max_tokens": 512
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    return f"Groq Error: {response.status_code} - {response.text}"

# Streamlit UI
st.set_page_config(page_title="Multimodal Visual Chatbot", layout="wide")
st.title("🧠 Multimodal Visual Chatbot (Groq + HF)")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_file.read())
        st.session_state.image_path = "temp_image.png"
        st.session_state.image = Image.open("temp_image.png").convert("RGB")
        st.image(st.session_state.image, caption="Uploaded Image", use_container_width=True)

        if "caption" not in st.session_state:
            with st.spinner("Generating caption..."):
                st.session_state.caption = generate_caption("temp_image.png")
            st.success("Caption generated!")

        st.write("📝 **Image Caption:**")
        st.write(st.session_state.caption)

# Chat area
st.header("💬 Chat with the Image")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask a question about the image..."):
    if "caption" not in st.session_state:
        st.warning("Please upload and analyze an image first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                vqa_answer = answer_with_sa2va("temp_image.png", prompt)
                groq_response = answer_with_groq(st.session_state.caption, vqa_answer, prompt)
                st.write(groq_response)
                st.session_state.messages.append({"role": "assistant", "content": groq_response})
