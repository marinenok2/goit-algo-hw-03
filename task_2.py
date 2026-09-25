import random


def get_numbers_ticket(min, max, quantity):
    """Повертає відсортований список унікальних випадкових чисел."""

    # Усі три параметри мають бути цілими числами.
    if type(min) is not int or type(max) is not int or type(quantity) is not int:
        return []

    # Перевіряємо дозволені межі та кількість чисел.
    available = max - min + 1

    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > available:
        return []

    # sample вибирає випадкові числа без повторів.
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортуємо список і повертаємо результат.
    numbers.sort()
    return numbers


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(10, 15, 7))  # [] — у діапазоні лише 6 чисел