from datetime import datetime


def get_days_from_today(date):
    """Повертає кількість днів від заданої дати до сьогодні."""
    try:
        # Перетворюємо рядок формату "РРРР-ММ-ДД" на дату без часу.
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        # Якщо дату записано неправильно, повертаємо None.
        return None

    # Беремо лише поточну дату, без годин і хвилин.
    today = datetime.today().date()

    # Для майбутньої дати різниця буде від’ємною.
    difference = today - given_date
    return difference.days