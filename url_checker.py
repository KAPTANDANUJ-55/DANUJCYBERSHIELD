from rapidfuzz import fuzz
import json
import re
from urllib.parse import urlparse

def load_keywords():
    with open("data/ur3l.json", "r") as f:
        return json.load(f)

# Suspicious shortened URLs jo commonly fraud mein use hote hain
SHORTENERS = ['bit.ly', 'tinyurl', 'goo.gl', 't.co', 'ow.ly', 'is.gd']

# Suspicious TLDs (top-level domains) - kuch shady countries ya generic suspicious
SUSPICIOUS_TLDS = ['.xyz', '.top', '.club', '.online', '.site', '.win', '.loan', '.info']

def scan_url(url, threshold=75):
    url_lower = url.lower()
    keywords = load_keywords()
    reasons = set()

    parsed = urlparse(url_lower)
    domain = parsed.netloc
    path = parsed.path

    # 1. Exact keyword match (word boundary)
    for kw in keywords:
        if re.search(r'\b' + re.escape(kw) + r'\b', url_lower):
            reasons.add(f"Keyword match: '{kw}'")

    # 2. Fuzzy matching for keywords (typos, tricks)
    for kw in keywords:
        score = fuzz.partial_ratio(kw, url_lower)
        if score >= threshold:
            reasons.add(f"Fuzzy match: '{kw}' (score: {score})")

    # 3. Check if domain is a shortened URL
    for shortener in SHORTENERS:
        if shortener in domain:
            reasons.add(f"Shortened URL detected: {shortener}")

    # 4. Suspicious TLD check
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            reasons.add(f"Suspicious TLD: {tld}")

    # 5. Multiple domain-like strings in path (possible phishing)
    domain_pattern = re.compile(r'[a-z0-9\-]+\.[a-z]{2,3}(\.[a-z]{2,3})?')
    domains_in_path = domain_pattern.findall(path)
    if len(domains_in_path) > 1:
        reasons.add("Multiple domain-like strings in URL path")

    if reasons:
        return "⚠️ Scam URL detected due to:\n- " + "\n- ".join(reasons)
    else:
        return "✅ URL looks BLOODY clean."

# Example test
if __name__ == "__main__":
    test_urls = [
        "http://secure-paypal.com-login.com",
        "https://bit.ly/3jkl9",
        "http://example.xyz/free-offer",
        "http://normalwebsite.com/path/page"
    ]
    for url in test_urls:
        print(f"Checking URL: {url}")
        print(scan_url(url))
        print("="*40)
