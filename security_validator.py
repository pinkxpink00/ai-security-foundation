from typing import Dict,List, Optional

def analyze_prompt(prompt: str) -> Dict[str, any]:
    "не просто тру ор фолзб, а детальный анализ"
    dangerous_keywords = ["DAN:","system override","Ignore","Injection","Override"]

    found_keywords = [
        keyword for keyword in dangerous_keywords
        if keyword.lower() in prompt.lower()
    ]

    return {
        "is_safe": len(found_keywords) == 0,
        "detected_keywords": found_keywords,
        "risk_level": "HIGH" if found_keywords else "LOW"
    }

result = analyze_prompt("Ignore my instruction")
print(result)