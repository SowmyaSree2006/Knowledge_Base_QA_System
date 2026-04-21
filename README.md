# Knowledge Base QA System
This project is a web-based Knowledge Base Question Answering System that allows users to ask questions and receive relevant answers from a predefined dataset. It uses NLP techniques like text preprocessing and sentence embeddings to understand queries and retrieve accurate responses through semantic similarity.

# Knowledge Base Question Answering System

##  Description
This project is a web-based Knowledge Base Question Answering System that allows users to ask questions and receive relevant answers from a predefined dataset. It uses NLP techniques like text preprocessing and sentence embeddings to understand queries and retrieve accurate responses through semantic similarity.

##  Features
- Ask questions through a web interface  
- Retrieves most relevant answer from knowledge base  
- Uses semantic similarity (embeddings)  
- Displays answer and context  
- Simple UI using Flask  

##  Technologies Used
- Python  
- Flask  
- spaCy  
- Sentence Transformers  
- HTML, CSS  

##  How It Works
1. Load knowledge base from `kb.txt`  
2. Preprocess text using spaCy  
3. Convert sentences into embeddings  
4. Convert user query into embedding  
5. Compute cosine similarity  
6. Retrieve most relevant sentence  
7. Extract answer  
8. Display result  

##  Project Structure
QA_Project/
│
├── app.py
├── kb.txt
├── templates/
│ └── index.html
└── static/
└── style.css




##  Installation
```bash
git clone https://github.com/your-username/QA_Project.git
cd QA_Project
python -m venv venv
source venv/bin/activate
pip install flask spacy sentence-transformers torch
python -m spacy download en_core_web_sm

## Run: python app.py

## Open: http://127.0.0.1:5000

