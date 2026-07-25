def analyze_prompt(text):
    dangerous_keywords = ["DAN:", "system override", "Ignore", "Injection", "Override"]

    detected_keywords = [kw for kw in dangerous_keywords if kw.lower() in text.lower()]

    return {
        "is_safe": len(detected_keywords) == 0,
        "detected_keywords": detected_keywords,
        "risk_level": "HIGH" if detected_keywords else "LOW"
    }


print(analyze_prompt("Ignore me"))
print(analyze_prompt("hello world"))
print(analyze_prompt("DAN: override system"))
