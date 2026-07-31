def has_number(text):
    return any(char for char in text if char.isdigit())


def test_has_number_with_digits():
    result = has_number("1234")
    assert result == True
    print("✅ Тест: with digits прошел!")

def test_has_number_without_digits():
    result = has_number("hello world")
    assert result == False
    print("✅ Тест: without digits прошел!")

def test_has_number_mixed():
    result = has_number("1234")
    assert result == True
    print("✅ Тест: mixed прошел!")

if __name__ == "__main__":
    test_has_number_with_digits()
    test_has_number_without_digits()
    test_has_number_mixed()