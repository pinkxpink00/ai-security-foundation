import re

def analyze_prompt_with_regex(text):
    patterns = {
        "ignore_attack": r"i.*g.*n.*o.*r.*e",
        "override_attack": r"o.*v.*e.*r.*r.*i.*d.*e",
        "dan_attack": r"d.*a.*n",
        "injection": r"inject",
    }

    detected = []

    for attack_name, pattern in patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            detected.append(attack_name)

    return {
        "is_safe": len(detected) == 0,
        "detected_attacks": detected,
        "risk_level": "HIGH" if detected else "LOW"
    }

# Тесты:
print(analyze_prompt_with_regex("Ignore me"))
print(analyze_prompt_with_regex("hello world"))
print(analyze_prompt_with_regex("i_g_n_o_r_e system"))


def test_regex_ignore_attack():
    result = analyze_prompt_with_regex("i_g_n_o_r_e system")
    assert result["is_safe"] == False
    assert "ignore_attack" in result["detected_attacks"]
    print("✅ Тест regex ignore прошел!")

def test_regex_safe():
    result = analyze_prompt_with_regex("hello world system")
    assert result["is_safe"] == True
    assert len(result["detected_attacks"]) == 0
    print("✅ Тест regex safe прошел!")

def test_regex_multiple_attacks():
    result = analyze_prompt_with_regex("ignore and override system")
    assert result["is_safe"] == False
    assert len(result["detected_attacks"]) >= 2
    print("✅ Тест regex multiple attacks прошел!")

if __name__ == "__main__":
    test_regex_ignore_attack()
    test_regex_safe()
    test_regex_multiple_attacks()