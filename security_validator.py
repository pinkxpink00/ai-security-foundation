def check_dangerous_words(text):
    dangerous_keywords = ["DAN:", "system override", "Ignore", "Injection", "Override"]

    results = []
    for keyword in dangerous_keywords:
        if keyword.lower() in text.lower():
            results.append((keyword.lower()) in text.lower())

    return any(results)

print(check_dangerous_words("Ignore me"))
print(check_dangerous_words("hello"))

