import re

pattern = r"ignore" # r meaning 'raw string'
text = "IGNORE me"

result = re.search(pattern, text, re.IGNORECASE)
print(result)