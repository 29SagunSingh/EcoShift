from transformers import pipeline
import requests
from bs4 import BeautifulSoup

classifier=pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def extract_claims(url):
    html=requests.get(url).text
    soup=BeautifulSoup(html, "html.parser")
    return soup.get_text()[:2000]

def analyze_claims(text):
    labels=["carbon neutral", "plastic-free", "ethical labor", "greenwashing"]
    return classifier(text, labels)

#Run demo
if __name__ == "__main__":
    sample_url="https://somebrand.com"
    claims=extract_claims(sample_url)
    result=analyze_claims(claims)
    print(result)