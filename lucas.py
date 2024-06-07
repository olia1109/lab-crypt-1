import random
import math
from rabin_miller import mod_pow as modular_exponentiation


def prime_factors(n):
    """Знаходить всі прості множники (числа, на які дане число може бути поділене без залишку) числа n."""
    factors = []
    # Перевіряємо, скільки разів число n ділиться на 2
    if n % 2 == 0:
        factors.append(2)
    while n % 2 == 0:
        n //= 2  # Ділимо n на 2 поки воно парне

    # Після видалення всіх множників 2, n має бути непарним
    # Тому можна перевіряти дільники з кроком 2 (тільки непарні числа)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in factors:
                factors.append(i)  # Додаємо i до списку множників, якщо воно ділить n
            n //= i  # Ділимо n на i доки воно ділиться націло

    # Якщо після обробки залишається число більше за 2, воно також простий множник
    if n > 2:
        factors.append(n)
    return factors


def lucas_test(n):
    """Перевіряє, чи є число n простим за допомогою тесту Лукаса."""
    if n == 1:
        return False  # 1 не є простим числом
    if n == 2:
        return True  # 2 є простим числом
    if n % 2 == 0:
        return False  # Парні числа більше за 2 не можуть бути простими

    # Знаходимо прості множники n-1 для подальшого тестування
    factors = prime_factors(n - 1)
    trial_count = 10  # Кількість спроб тесту

    # Проводимо тест Лукаса задану кількість разів
    for _ in range(trial_count):
        a = random.randint(2, n - 2)
        if modular_exponentiation(a, n - 1, n) != 1:
            return False  # Якщо a^(n-1) % n != 1, то n не є простим
        flag = True
        for factor in factors:
            if modular_exponentiation(a, (n - 1) // factor, n) == 1:
                flag = False
                break
        if flag:
            return True  # Якщо умови виконуються для всіх множників, n ймовірно просте

    return False  # Якщо жоден тест не підтвердив простоту, n не є простим
