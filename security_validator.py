def check_dangerous_words(text):
    dangerous_keywords = ["DAN:", "system override", "Ignore", "Injection", "Override"]
    return any(keyword.lower() in text.lower() for keyword in dangerous_keywords)

print(check_dangerous_words("Ignore me"))
print(check_dangerous_words("hello"))

