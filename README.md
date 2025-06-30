# 🧠 Visual QA Chatbot

A powerful Streamlit-based visual chatbot that combines advanced image analysis with intelligent conversation capabilities. This application uses state-of-the-art AI models for image captioning, visual question answering, and enhanced text generation.

## ✨ Features

- **🖼️ Image Captioning**: Detailed descriptions using Joy Caption model via Gradio API
- **❓ Visual Question Answering**: Answer questions about uploaded images using Sa2VA model
- **🤖 Intelligent Responses**: Enhanced answers using Groq's language models
- **💬 Interactive Chat**: Clean and intuitive Streamlit interface
- **🔄 Real-time Processing**: Fast API-based model inference
- **📱 Responsive Design**: Works on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key
- Hugging Face token (optional, for enhanced features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivaraj245/visual-qa-chatbot.git
   cd visual-qa-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HUGGINGFACE_TOKEN=your_huggingface_token_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🔑 API Keys Setup

### Groq API Key (Required)
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and add to your `.env` file

### Hugging Face Token (Optional)
1. Visit [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Create a new token with read permissions
3. Copy and add to your `.env` file

## 🎯 How to Use

1. **Upload an Image**: Use the sidebar to upload JPG, JPEG, or PNG files
2. **Automatic Analysis**: The app will automatically generate a detailed caption
3. **Ask Questions**: Use the chat interface to ask questions about the image
4. **Get Answers**: Receive intelligent responses combining visual analysis and AI reasoning

## 🤖 Models Used

- **Image Captioning**: `fancyfeast/joy-caption-beta-one` (via Gradio API)
- **Visual Q&A**: `fffiloni/Sa2VA-simple-demo` (via Gradio API)
- **Text Generation**: `llama-3.1-8b-instant` (via Groq API)

## 📁 Project Structure

```
visual-qa-chatbot/
├── app.py                 # Main Streamlit application (not included in repo)
├── main.py               # Alternative implementation (not included in repo)
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create locally)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🛠️ Technical Details

### Architecture
- **Frontend**: Streamlit for web interface
- **Backend**: Gradio Client API for model inference
- **Image Processing**: PIL for image handling
- **API Integration**: Requests for HTTP calls

### Supported Image Formats
- JPEG/JPG
- PNG
- GIF
- BMP
- TIFF

### Performance
- **Response Time**: ~2-5 seconds per query
- **Image Size**: Supports up to 10MB images
- **Concurrent Users**: Scalable with Streamlit sharing

## 🔧 Troubleshooting

### Common Issues

**API Key Errors**
- Verify your API keys are correctly set in `.env`
- Check if your Groq API key has sufficient credits
- Ensure no extra spaces in environment variables

**Model Loading Issues**
- Check your internet connection
- Try refreshing the page
- Verify Gradio services are accessible

**Image Upload Problems**
- Ensure image file is under 10MB
- Check if image format is supported
- Try converting image to PNG format

### Performance Optimization
```bash
# For better performance, consider upgrading pip packages
pip install --upgrade streamlit gradio-client requests
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing access to state-of-the-art models
- [Groq](https://groq.com/) for fast inference capabilities
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Gradio](https://gradio.app/) for model hosting and API access

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/shivaraj245/visual-qa-chatbot/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

## 🚀 Future Enhancements

- [ ] Support for video analysis
- [ ] Multiple image comparison
- [ ] Custom model fine-tuning
- [ ] Voice interaction capabilities
- [ ] Multi-language support
- [ ] Export conversation history

---

**Made with ❤️ using Streamlit and AI**
