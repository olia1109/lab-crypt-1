import random

# Реалізувати операцію швидкого піднесення до степеню по модулю
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  
    while exponent > 0:
        if (exponent % 2) == 1:  # Якщо поточний біт експоненти дорівнює 1
            result = (result * base) % modulus  # Множимо результат на поточне значення основи
        base = (base * base) % modulus  # Підносимо основу до квадрату
        exponent //= 2  # Зміщуємо біти експоненти вправо
    return result

# Miller–Rabin primality test
def miller_rabin_test(d, n):
    """Ця функція викликається для всіх k ітерацій.
    Повертає False, якщо n складене,
    Повертає True, якщо n ймовірно просте.
    d — непарне число таке, що d*2^r = n-1 для деякого r >= 1"""
    a = 2 + random.randint(0, n - 4)  # Випадкова основа для тестування

    x = modular_exponentiation(a, d, n)  # Обчислюємо a^d % n

    if x == 1 or x == n - 1:
        return True  # n ймовірно просте

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False  # n складене, оскільки ми знайшли нетривіальний квадратний корінь з одиниці
        if x == n - 1:
            return True  # n ймовірно просте

    return False  # n складене, оскільки не пройшло умови

def is_prime_rabin_miller(n, iterations):
    """Перевіряє, чи є число n простим, використовуючи k ітерацій тесту Міллера-Рабіна."""
    if n <= 1 or n == 4:
        return False  # Числа менше або рівні 1, а також число 4 не є простими
    if n <= 3:
        return True  # Числа 2 і 3 є простими

    # Знаходимо d таке, що n = 2^d * r + 1 для деякого r >= 1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Повторюємо тест Міллера-Рабіна задану кількість разів для збільшення ймовірності визначення простоти
    for _ in range(iterations):
        if not miller_rabin_test(d, n):
            return False  # Якщо хоча б один тест показує, що n складене, повертаємо False
    return True  # Якщо всі тести показали, що n ймовірно просте, повертаємо True
