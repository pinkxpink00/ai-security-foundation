import re

from regex import pattern


def detect_injection_advanced(text):
    pattern = r"i.*g.*n.*o.*r.*e"

    if re.search(pattern, text, re.IGNORECASE):
        return True
    return False

print(detect_injection_advanced("ignore"))           # True
print(detect_injection_advanced("i g n o r e"))      # True (с пробелами)
print(detect_injection_advanced("IGNORE"))           # True
print(detect_injection_advanced("hello world"))      # False