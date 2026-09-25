import re


def normalize_phone(phone_number):
    """Прибирає зайві символи й додає код країни за потреби."""
    digits = re.sub(r"\D", "", phone_number)

    # Якщо в початковому номері вже був міжнародний код із «+».
    if phone_number.strip().startswith("+"):
        return "+" + digits

    # Якщо є код 380, але немає «+».
    if digits.startswith("380"):
        return "+" + digits

    # Якщо коду немає, додаємо український +38.
    return "+38" + digits