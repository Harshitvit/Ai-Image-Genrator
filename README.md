# Ai-Image-Genrator

This is a simple AI-powered image generator using **Flask** and **Stability AI's API**. Users can input a text prompt, and the application will generate an image based on the provided prompt.

## 🚀 Features
- Generate AI-powered images from text prompts
- Backend powered by **Flask**
- Uses **Stability AI SDK** for image generation
- Stores generated images in a local directory
- Simple and responsive frontend

## 🛠️ Installation

### 1. Clone the Repository
```sh
git clone https://github.com/Harshitvit/ai-image-generator.git
cd ai-image-generator
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add your **Stability AI API Key**:
```sh
STABILITY_KEY=your_api_key_here
```

## 🚀 Running the Application
```sh
python app.py
```
The application will start at `http://127.0.0.1:5000/`

## 🖼️ Usage
1. Open the application in your browser.
2. Enter a text prompt in the input field.
3. Click the **Generate Image** button.
4. The AI-generated image will appear below.

## 📁 Project Structure
```
├── static/
│   ├── images/   # Stores generated images
├── templates/
│   ├── index.html  # Frontend UI
├── app.py  # Flask Backend
├── requirements.txt  # Required dependencies
├── .env (to be created)  # API Key storage
├── README.md  # Project Documentation
```

## 🛠️ Technologies Used
- **Flask** (Web framework)
- **Stability AI SDK** (Image generation)
- **Pillow** (Image processing)
- **Python-dotenv** (Environment variable management)

## 🤖 API Reference
- Stability AI: [API Documentation](https://platform.stability.ai/docs)

## 🔥 Future Enhancements
- Improve UI with **Tailwind CSS**
- Add support for multiple image resolutions
- Implement user authentication

## 📝 License
This project is open-source and available under the **MIT License**.

