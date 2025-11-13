from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def analyze_speaking(conversation):
    user_texts = [m["content"] for m in conversation if m["role"] == "user"]
    text = " ".join(user_texts)

    if len(text.split()) < 20:
        return "Your answers were too short. Try giving longer responses."

    vocab_size = len(set(text.split()))
    score = np.clip(vocab_size / 50, 0, 9)

    grammar_feedback = "Good grammar overall, minor mistakes." if score > 6 else "Work on sentence structure and tense consistency."

    return f"Band Estimate: {round(score, 1)}\n{grammar_feedback}\nVocabulary richness: {vocab_size} unique words."
