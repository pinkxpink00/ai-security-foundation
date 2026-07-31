import re

def detect_dan_attack(text):
    pattern = r"dan"

    if re.search(pattern, text, re.IGNORECASE):
        return True
    else:
        return False

print(detect_dan_attack("DAN: do anything"))
print(detect_dan_attack("dan: override"))
print(detect_dan_attack("hello world"))