# NOTE NINJA REALTIME 🎙️📜
A real-time transcription, summarization, and text-to-speech application with a floating window UI.

<!-- Replace with the actual path to your logo -->

# 📝 Overview
NOTE NINJA REALTIME is an AI-powered tool that allows users to:
✅ Transcribe speech to text in real time using Whisper
✅ Summarize transcriptions with BART
✅ Play the summarized text using Text-to-Speech (TTS)
✅ Convert summaries into PDFs
✅ Translate summaries into different languages
✅ Switch between Light Mode and Dark Mode

# 🚀 Features
--🎤 Real-Time Transcription
--Uses OpenAI’s Whisper model for accurate speech-to-text conversion.
--Captures and updates text in real time.
--✨ Summarization
Uses BART (Facebook’s model) for extracting key points from transcriptions.
--Enhances readability and saves time.
🔊 Text-to-Speech (TTS)
Converts text into speech using pyttsx3.
Reads summaries aloud for better accessibility.
📄 PDF Conversion
Exports transcriptions and summaries as PDF files.
🌍 Translation Support
Supports multiple languages like Hindi, Nepali, Odia, Bengali.
🌓 Dark Mode Toggle
Allows users to switch between Light Mode and Dark Mode with a button.
🖥️ UI Preview
<!-- Replace with the actual path -->

# ⚙️ Installation

1️⃣ Clone the Repository
https://github.com/MR-SAJAN-SAH/Note_Ninza.git
cd NOTE_NINJA_REALTIME

2️⃣ Set Up a Virtual Environment (Recommended)
python -m venv venv 

venv\Scripts\activate  # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

# Now, you need to download the whisper and bart model to use it: Load the base Whisper model and processor

rom transformers import WhisperProcessor, WhisperForConditionalGeneration

whisper_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")

whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-base")
 
# Load the BART base model and tokenizer

from transformers import BartTokenizer, BartForConditionalGeneration

bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-base")

bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")

# Also you need to configure the sound driver channels accordinglt otherwise it wonn't work properly


# ▶️ Usage
Run the application:

python src/app.py

Click "Start" to begin recording.

Click "Stop" to end transcription.

Click "Play" to hear the summarized text.

Click "PDF" to save the summary.

Use "Translate" to convert the summary into another language.

Use the Dark Mode Toggle on the top right to switch themes.

# 📌 Requirements
Python 3.8+

pip install -r requirements.txt
💡 Future Enhancements
✔️ Support for additional languages
✔️ Cloud-based storage integration
✔️ Improved UI with customizable themes

# 📜 License
MIT License © 2025 sajan kumar sah

# 🙌 Contributors
👤 Sajan Kumar Sah
