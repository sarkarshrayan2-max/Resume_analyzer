# 📄 AI Resume Analyzer & Career Advisor

An AI-powered Resume Analyzer built using Streamlit, LangChain, Groq, FAISS, Sentence Transformers, and Adzuna Job Market API.

The application helps users:

* Extract skills from resumes
* Compare resumes with job descriptions
* Calculate ATS-style match scores
* Identify missing skills
* Ask questions about resumes using RAG
* Predict suitable career paths
* Analyze live job market demand
* Discover skill gaps based on real-world job postings

---

## 🚀 Features

### 📄 Resume Parsing

* Upload PDF resumes
* Upload DOCX resumes
* Automatic text extraction

### 🧠 AI Skill Extraction

* Uses Groq LLM
* Extracts technical and soft skills
* Returns structured skill lists

### 🎯 ATS Job Matching

* Compare resume against any job description
* Skill match scoring
* Semantic similarity scoring
* Final weighted match score
* Missing skill detection
* AI-generated match explanation

### 💬 Resume Q&A (RAG)

* FAISS Vector Database
* HuggingFace Embeddings
* Retrieval Augmented Generation (RAG)

Ask questions like:

* What projects has the candidate built?
* What programming languages does the candidate know?
* Does the candidate have machine learning experience?

### 🚀 Career Path Predictor

Analyze:

* Skills
* Projects
* Experience
* Tools
* Education

Predict:

* Top Career Fields
* Best Target Role
* Skill Gaps
* Learning Roadmap
* Next Project Suggestions

### 📈 Live Job Market Analysis

Powered by Adzuna API.

Features:

* Fetches current job listings
* Extracts market-demanded skills
* Compares resume skills against market skills
* Calculates Market Fit Score
* Shows missing market skills
* Recommends skills to learn next

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM & AI

* Groq
* LangChain
* LangChain Core

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* FAISS

### Resume Processing

* PyPDF
* Python-Docx

### Job Market Analysis

* Adzuna API

### Machine Learning

* Scikit-Learn

### Deployment

* Streamlit Cloud
* GitHub Actions CI/CD

---

## 📂 Project Structure

```text
resume_analyzer/
│
├── app.py
├── config.py
├── llm.py
├── matcher.py
├── rag.py
├── prompts.py
├── job_market.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

ADZUNA_APP_ID=your_adzuna_app_id

ADZUNA_APP_KEY=your_adzuna_app_key
```

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

## 🔄 CI/CD

GitHub Actions automatically:

* Installs dependencies
* Checks syntax
* Validates project files

Runs on:

* Push to main
* Pull Requests

---

## 📌 Future Improvements

* JSON-based career prediction output
* Resume improvement recommendations
* Cover letter generation
* Multi-resume comparison
* Salary trend analysis
* Personalized learning roadmap
* Cloud deployment recommendations

---

## 👨‍💻 Author

Shrayan Sarkar

sarkarshrayan2@gmail.com

---

Built with using Streamlit, LangChain, Groq, FAISS, and Adzuna API.
