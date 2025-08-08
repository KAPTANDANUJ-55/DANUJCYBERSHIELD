from rapidfuzz import fuzz
import json
import re

def load_keywords():
    with open("data/scamnum.json", "r") as f:
        return json.load(f)  # Assume it's a list of scam number patterns/keywords

def scan_number(numn, threshold=75):
    """
    numn: string or number input (phone number as string preferred)
    threshold: for fuzzy matching score
    """
    # Convert number to string for processing
    numb = str(numn).lower()
    keywords = load_keywords()

    found = []

    # 1. Regex exact word boundary match
    for kw in keywords:
        # Lowercase kw too
        pattern = r'\b' + re.escape(kw.lower()) + r'\b'
        if re.search(pattern, numb):
            found.append(kw)

    # 2. Fuzzy matching for tricky scams if regex no match
    if not found:
        for kw in keywords:
            score = fuzz.partial_ratio(kw.lower(), numb)
            if score >= threshold:
                found.append(kw)

    if found:
        return f"⚠️ Possible scam number detected: {', '.join(set(found))}"
    else:
        return "✅ NUMBER LOOKS BLOODY CLEAN."

# Example usage
if __name__ == "__main__":
    # Number as string better for partial matching and regex
    nu = "+918047592314"
    print(scan_number(nu))
