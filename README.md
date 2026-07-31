# AI Security Foundation

Проект для обучения AI Security и Python. Детектирование prompt injection атак для LLM систем.

## 📚 Прогресс обучения

- **День 1:** Type hints, базовая валидация промптов
- **День 2:** List Comprehension, any() функция, детальный анализ
- **День 3-4:** Unit Tests, практика с функциями

## 🚀 Функции

### `analyze_prompt(text)`
Анализирует текст на наличие опасных слов для prompt injection атак.

**Возвращает словарь:**
```python
{
    "is_safe": bool,                    # True если безопасно
    "detected_keywords": list,          # Найденные опасные слова
    "risk_level": str                   # "HIGH" или "LOW"
}
```

**Пример:**
```python
from security_validator import analyze_prompt

result = analyze_prompt("Ignore my instruction")
print(result)
# {'is_safe': False, 'detected_keywords': ['Ignore'], 'risk_level': 'HIGH'}
```

### `check_dangerous_words(text)`
Быстрая проверка: возвращает True если найдено опасное слово, False если безопасно.

**Пример:**
```python
check_dangerous_words("hello world")  # False (безопасно)
check_dangerous_words("Ignore me")    # True (опасно)
```

### `has_number(text)`
Проверяет содержит ли текст цифры.

**Пример:**
```python
has_number("hello123")   # True
has_number("hello")      # False
```

## 🧪 Unit Tests

Запуск всех тестов:
```bash
python -m pytest test_security_validator.py
```

Или просто:
```bash
python test_security_validator.py
```

**Тесты покрывают:**
- ✅ Обнаружение injection атак
- ✅ Проверка безопасных текстов
- ✅ Работа с разными регистрами (case insensitive)
- ✅ Обнаружение нескольких опасных слов
- ✅ Проверка цифр в тексте

## 🔍 Опасные слова

Текущий список обнаруживаемых атак:
- `"Ignore"` — игнорирование инструкций
- `"Override"` — перекрытие системы
- `"DAN:"` — "Do Anything Now" атака
- `"Injection"` — прямое упоминание инъекции
- `"system override"` — системное перекрытие

## 💡 Ключевые концепции

### List Comprehension
```python
detected = [word for word in dangerous_words if word.lower() in text.lower()]
```

### any() функция
```python
return any(keyword.lower() in text.lower() for keyword in dangerous_keywords)
```

### Unit Tests с assert
```python
def test_injection_detected():
    result = analyze_prompt("Ignore me")
    assert result["is_safe"] == False
```

## 📈 Что дальше

- [ ] Regex паттерны для более сложных атак
- [ ] Claude API интеграция
- [ ] Multi-agent система
- [ ] Web API с Flask/FastAPI
- [ ] Логирование и аудит

## 👨‍💻 Автор

Обучение AI Security на Python. День 3-4 из 6-месячного плана.

## 📝 Структура проекта