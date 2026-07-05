# 🎙️ Audio Question Answering System using Whisper + RAG

An AI-powered application that converts audio into searchable knowledge using **OpenAI Whisper** and **Retrieval-Augmented Generation (RAG)**. The system transcribes audio, generates semantic embeddings, retrieves the most relevant transcript segments, and answers user questions with accurate timestamps.

---

## 🚀 Features

- 🎤 Convert MP3 audio to text using Whisper
- 📝 Generate timestamped transcript chunks
- 🔍 Create semantic embeddings using BGE-M3
- 📚 Store transcript embeddings for retrieval
- 🤖 Answer user questions using RAG and Llama 3.2
- ⏱️ Return the exact audio timestamp containing the answer
- 📂 Process multiple audio files automatically

---

## 🛠️ Tech Stack

- Python
- OpenAI Whisper
- Ollama
- Llama 3.2
- BGE-M3 Embedding Model
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FFmpeg

---

## 📂 Project Structure

before starting this project should contain audio file "audio" / vedio file "vedio"  < where audios and vedios are ready to be converted to mp3 and json>
```
Audio-RAG-Assistant/
│
├── mp3_conversion.py          # Converts audio into required format
├── mp3_to_json.py             # Transcribes audio using Whisper
├── embed_with_jsons.py        # Creates vector embeddings
├── embed_process_to_rag.py    # Retrieves relevant chunks and generates answers
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Workflow

```
Audio Files
      │
      ▼
FFmpeg Audio Processing
      │
      ▼
Whisper Speech-to-Text
      │
      ▼
Timestamped JSON Transcripts
      │
      ▼
Embedding Generation (BGE-M3)
      │
      ▼
Vector Storage
      │
      ▼
Semantic Search
      │
      ▼
Llama 3.2 (RAG)
      │
      ▼
Answer with Relevant Timestamp
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Audio-RAG-Assistant.git

cd Audio-RAG-Assistant
```

### 2. Create a virtual environment (Optional)

```bash
conda create -n whisper_env python=3.12
conda activate whisper_env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Ensure FFmpeg is installed and added to your system PATH.

### 5. Install Ollama

Download and install Ollama.

Pull the required models:

```bash
ollama pull llama3.2

ollama pull bge-m3
```

---

## ▶️ Usage

### Step 1 – Convert audio files

```bash
python mp3_conversion.py
```

### Step 2 – Generate transcripts

```bash
python mp3_to_json.py
```

### Step 3 – Generate embeddings

```bash
python embed_with_jsons.py
```

### Step 4 – Ask questions

```bash
python embed_process_to_rag.py
```

---

## 💡 Example

### User Question

```
When does the speaker conclude the discussion?
```

### Output

```
Answer:
The speaker concludes the discussion between
21.26s and 23.76s.

Audio Title:
speech-sample

Audio Number:
29496
```

---

## 🎯 Skills Demonstrated

- Speech Recognition
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Prompt Engineering
- Large Language Models (LLMs)
- Information Retrieval
- Python Development

---

## ⭐ If you found this project useful, consider giving it a star!
