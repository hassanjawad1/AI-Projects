import requests
import time
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HEADERS = {
    "Authorization": "Bearer your-api"  # Replace with your actual token
}

def chunk_text(text, max_tokens=500):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    token_count = 0

    for sentence in sentences:
        tokens = len(sentence.split())
        if token_count + tokens <= max_tokens:
            current_chunk.append(sentence)
            token_count += tokens
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            token_count = tokens
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_text(text, section):
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        payload = {
            "inputs": chunk,
            "parameters": {
                "min_length": 40,
                "max_length": 150,
                "do_sample": False
            }
        }
        for attempt in range(3):
            try:
                response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
                response.raise_for_status()
                summary = response.json()[0]['summary_text']
                summaries.append(summary)
                break
            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error: {e}")
                if "Model too busy" in str(e) or response.status_code == 500:
                    time.sleep(5)
                    continue
                summaries.append(f"⚠️ HTTP error summarizing {section}: {e}")
                break
            except Exception as e:
                summaries.append(f"⚠️ Unknown error summarizing {section}: {str(e)}")
                break

    return " ".join(summaries)
