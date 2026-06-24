# mpls.hassan
import ssl
import sys

import nltk
from nltk.tokenize import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# macOS fix: use unverified SSL context for NLTK downloads
if sys.platform == "darwin":
    ssl._create_default_https_context = ssl._create_unverified_context

# required files for tokenizing
nltk.download("punkt_tab", quiet=True)
nltk.download("vader_lexicon", quiet=True)

analyzer = SentimentIntensityAnalyzer()


def get_sentences(text: str) -> list[str]:
    if (not text) or (not text.strip()):
        return []
    sentences = sent_tokenize(text)
    if not sentences:
        return [text.strip()]
    return sentences


def analyze_sentiments(sentences: list[str]) -> list[dict[str, float]]:
    return [analyzer.polarity_scores(s) for s in sentences]
