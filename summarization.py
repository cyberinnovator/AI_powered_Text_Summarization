# summarization.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from keybert import KeyBERT
from newspaper import Article

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

kw_model = KeyBERT(model='all-MiniLM-L6-v2')

def fetch_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_and_extract_keywords(url):
    try:
        content = fetch_article_content(url)

        # Summarize
        inputs = tokenizer(content, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs.input_ids, max_length=150, min_length=30,
                                     length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Extract keywords
        keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(1, 2),
                                             stop_words='english', top_n=10)
        keywords = [kw[0] for kw in keywords]

        return summary, keywords
    except Exception as e:
        return f"Error: {str(e)}", []
