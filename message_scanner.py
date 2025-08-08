from rapidfuzz import fuzz
import json
import re

def load_keywords():
    with open("data/scammessage.json", "r") as f:
        return json.load(f)

def scan_message(message, threshold=75):
    message = message.lower()
    keywords = load_keywords()

    found = []

    # 1. Regex exact word boundary match
    for kw in keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', message):
            found.append(kw)

    # 2. Fuzzy matching for tricky scams if regex no match
    if not found:
        for kw in keywords:
            score = fuzz.partial_ratio(kw, message)
            if score >= threshold:
                found.append(kw)

    if found:
        return f"⚠️ Possible scam keywords detected: {', '.join(set(found))}"
    else:
        return "✅ Message looks BLOODY clean."

# Example usage
if __name__ == "__main__":
    test_msg = "Congratulations! You won the lotery prize."
    print(scan_message(test_msg))
