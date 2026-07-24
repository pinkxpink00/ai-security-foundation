from typing import List, Optional

def validate_prompt(prompt: str) -> bool:
    "проверяем промт на безопасность"
    dangerous_keywords = ["injection","override"]
    return not any(keyword in prompt.lower() for keyword in dangerous_keywords)


print(validate_prompt("hello world"))
print(validate_prompt("Ignore my instruction"))