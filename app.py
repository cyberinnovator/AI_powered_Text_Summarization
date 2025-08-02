from flask import Flask, render_template, request
from summarization import summarize_and_extract_keywords

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    keywords = []
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            summary, keywords = summarize_and_extract_keywords(url)
    return render_template("index.html", summary=summary, keywords=keywords)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from summarization import summarize_and_extract_keywords

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    keywords = []
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            summary, keywords = summarize_and_extract_keywords(url)
    return render_template("index.html", summary=summary, keywords=keywords)

if __name__ == "__main__":
    app.run(debug=True)
