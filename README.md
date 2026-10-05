# PrivaNote AI

**PrivaNote AI** is a privacy-first, locally hosted AI study tool built for the Hacktoberfest 2026 **"Build for a Friend" Weekend Challenge**.

It transforms messy, unstructured class notes into clear summaries, key concepts, and custom multiple-choice quizzes, helping students study more effectively without compromising their data privacy.

## How It Works

PrivaNote AI uses an open-weight AI model that runs locally on your machine, keeping your academic notes on your device rather than sending them to a proprietary cloud AI service.

* **Frontend:** A lightweight, interactive web interface built with [Streamlit](https://streamlit.io/).
* **AI Engine:** Google's open-weight [Gemma 2B](https://ai.google.dev/gemma) model.
* **Local Inference:** [Ollama](https://ollama.com/) runs the model directly on your hardware.
* **Privacy First:** Your notes are processed locally, with no external AI API required.
* **Cost-Effective:** No paid AI API calls are needed.

## Prerequisites

Before running PrivaNote AI, ensure you have the following installed:

1. **Python 3.8 or later** - [Download Python](https://www.python.org/downloads/)
2. **Ollama** - [Download Ollama](https://ollama.com/download)

## How to Run Locally

Follow these steps to run PrivaNote AI on your machine.

### 1. Download the Gemma Model

Open PowerShell or your terminal and run:

```bash
ollama run gemma:2b
```

This downloads the Gemma 2B model the first time you run it. The download may take a few minutes, depending on your internet connection.
Once the model starts, you can enter a prompt to test it. 

### 2. Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/mohisha1205/privanote-ai.git
cd privanote-ai
```

### 3. Install Dependencies

Install the required Python packages using the project's `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

On Windows, if `python` points to a different installation, you can try:

```powershell
py -m pip install -r requirements.txt
```

### 4. Launch the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Alternatively, on Windows:

```powershell
py -m streamlit run app.py
```

Streamlit will provide a local URL, usually:

**http://localhost:8501**

Open the URL in your browser, paste your class notes into the input box, and click **Generate Study Material** to create your study resources.

## Features

* **Smart Summaries:** Convert lengthy notes into concise, easy-to-understand summaries.
* **Key Concepts:** Identify the most important concepts from your notes.
* **AI-Generated Quizzes:** Generate multiple-choice questions to test your understanding.
* **Answer Explanations:** Review the correct answers and understand why they are correct.
* **Local AI Processing:** Keep your academic notes on your own machine without requiring a proprietary cloud AI API.

## Privacy by Design

PrivaNote AI is designed to process study material locally using Ollama and Gemma. Your notes do not need to be sent to an external AI service.

The application requires an internet connection for initial setup and model downloads. Once the required software and model are installed, AI generation can run locally without an internet connection.

## Built For

PrivaNote AI was created for the Hacktoberfest 2026 **"Build for a Friend" Weekend Challenge**, with the goal of making studying easier, more accessible, and more private for students.

---

**Study smarter. Keep your notes private. 📚🔒**
