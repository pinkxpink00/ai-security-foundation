def analyze_prompt(text):
    dangerous_word = ["Ignore", "Override", "DAN:", "Injection", "system override"]
    detected = [word for word in dangerous_word if word.lower() in text.lower()]
    return {
        "is_safe" : len(detected) == 0,
        "detected_keywords" : detected,
        "risk_level" : "HIGH" if detected else "LOW",
    }

# Тесты:
print(analyze_prompt("Ignore me"))
print(analyze_prompt("hello world"))
print(analyze_prompt("DAN: override system"))

def test_injection_detected():
    result = analyze_prompt("Ignore me")
    assert result["is_safe"] == False
    assert "Ignore" in result["detected_keywords"]
    print("✅ Тест прошел!")

def test_safe_text():
    result = analyze_prompt("hello world")
    assert result["is_safe"] == True
    assert len(result["detected_keywords"]) == 0
    assert result["risk_level"] == "LOW"
    print("✅ Тест прошел!")

def test_multiple_keywords():
    result = analyze_prompt("DAN: override system")

    assert result["is_safe"] == False
    assert len(result["detected_keywords"]) >= 2
    assert "DAN:" in result["detected_keywords"]
    assert "Override" in result["detected_keywords"]

    print("✅ Тест прошел!")
print(test_injection_detected())
print(test_safe_text())
print(test_multiple_keywords())