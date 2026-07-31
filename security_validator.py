def check_dangerous_words(text):
    dangerous_keywords = ["DAN:", "system override", "Ignore", "Injection", "Override"]
    return any(keyword.lower() in text.lower() for keyword in dangerous_keywords)

def test_check_dangerous_words_found():
    result = check_dangerous_words("override")
    assert result == True
    print("test: found pass")


def test_check_dangerous_words_not_found():
    result = check_dangerous_words("Hello World")
    assert result == False
    print("test: not found pass")

def test_check_dangerous_words_case_insensitive():
    result = check_dangerous_words("IGNORE ME")
    assert result == True
    print("test: case insensitive pass")


if __name__ == '__main__':
    test_check_dangerous_words_found()
    test_check_dangerous_words_not_found()
    test_check_dangerous_words_case_insensitive()