from flask import Flask, render_template, request
import spacy
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

# Load knowledge base
with open("kb.txt", "r") as f:
    kb = f.read().replace("\n", " ")

# Process text
nlp = spacy.load("en_core_web_sm")
doc = nlp(kb)
sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

# Load embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to get answer
def get_answer(question):
    # Encode question and sentences
    q_embed = embed_model.encode(question)
    s_embed = embed_model.encode(sentences)

    # Compute similarity
    scores = util.cos_sim(q_embed, s_embed)

    # Get best sentence
    best_idx = scores.argmax()
    context = sentences[best_idx]

    # Extract short answer (rule-based)
    if " is " in context:
        answer = context.split(" is ")[1].split(".")[0]
    else:
        answer = context

    return answer, context


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    context = ""

    if request.method == "POST":
        question = request.form["question"]
        answer, context = get_answer(question)

    return render_template("index.html", answer=answer, context=context)


if __name__ == "__main__":
    app.run(debug=True)