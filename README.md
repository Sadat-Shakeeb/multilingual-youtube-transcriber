# 🎧 YouTube to Roman Urdu Converter

An AI-powered web application that converts **Urdu and English YouTube videos into Roman Urdu** using Speech Recognition and Large Language Models.

🔗 **Live App:**  
https://huggingface.co/spaces/shakeeb08/youtube-to-roman-urdu

---

## 🚀 Project Overview

This application automates the following pipeline:

```

YouTube URL
↓
Audio Extraction (yt-dlp)
↓
Speech-to-Text (Whisper ASR)
↓
LLM Processing (Gemini)
↓
Roman Urdu Transcript Output

````

The system supports:

- Urdu audio → Roman Urdu  
- English audio → Roman Urdu  

---

## 🧠 Core Features

- ✅ Automatic language detection (Urdu / English)
- ✅ Chunk-based LLM processing to avoid token overflow
- ✅ Clean, interactive Streamlit interface
- ✅ Modular architecture (downloader, transcriber, romanizer)
- ✅ Secure API key management using environment variables
- ✅ Docker-based deployment support

---

## 🏗 Architecture Design

The application follows a modular pipeline architecture:

### 1️⃣ Downloader Module
- Uses `yt-dlp` to extract audio from YouTube videos.

### 2️⃣ Transcriber Module
- Uses `faster-whisper` for efficient speech recognition.
- Detects source language automatically.

### 3️⃣ Romanizer Module
- Uses Google Gemini LLM.
- Converts:
  - Urdu script → Roman Urdu
  - English → Roman Urdu
- Implements chunking to handle long transcripts safely.

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit**
- **faster-whisper**
- **yt-dlp**
- **Google Gemini API**
- **Docker (for cloud deployment)**

---

## 📸 Application Screenshots

### 🏠 Home Interface

![Home Screenshot 1](https://github.com/Sadat-Shakeeb/multilingual-youtube-transcriber/blob/0f71957a1565056928b39831eca587c888dfc001/assets/image1.png)

![Home Screenshot 2](https://github.com/Sadat-Shakeeb/multilingual-youtube-transcriber/blob/0f71957a1565056928b39831eca587c888dfc001/assets/image2.png)

---

### 📝 Sample Output (Roman Urdu Transcript)

![Sample Output](https://github.com/Sadat-Shakeeb/multilingual-youtube-transcriber/blob/0f71957a1565056928b39831eca587c888dfc001/assets/image3.png)

---

## 📦 Local Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Sadat-Shakeeb/multilingual-youtube-transcriber.git
cd multilingual-youtube-transcriber
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv yt_env
yt_env\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Gemini API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🌍 Deployment Notes

The app has been deployed on Hugging Face Spaces.

While deploying, the following real-world constraints were encountered:

* File watcher (inotify) limits on cloud infrastructure
* JavaScript runtime requirements for yt-dlp
* Network restrictions on some free-tier environments

These were addressed via:

* Streamlit configuration tuning
* Deployment strategy adjustments
* Modular system redesign

---

## 🎯 Key Engineering Learnings

* Handling cloud deployment limitations
* Managing environment secrets securely
* Designing chunk-based LLM pipelines
* Separating data ingestion from ML processing
* Debugging container health checks
* Optimizing Whisper performance on CPU

---

## 📌 Resume-Ready Project Description

Multilingual AI web application that converts Urdu and English YouTube videos into Roman Urdu using Whisper ASR and Gemini LLM. Designed with chunk-based LLM processing to handle long transcripts and deployed using Streamlit with secure API key management.

---

## 🔮 Future Improvements

* Direct audio file upload support
* Support for additional languages
* Migration to updated Gemini SDK
* Improved transcription accuracy tuning
* Background job processing for long videos

---

## 📄 License

MIT License
