import random
from rabin_miller import isPrimeRM


# Передбачити пошук простих чисел з заданою “бітністю”. (степені двійки)
def generate_prime(bits):
    if bits <= 1:
        return None # Число повинно бути хоча б двобітним

    while True:
        # Генеруємо випадкове число заданої бітності. Використання random.getrandbits(bits) дозволяє отримати
        # число з вказаною кількістю бітів, що забезпечує високий рівень випадковості та контроль над розміром числа
        candidate = random.getrandbits(bits)

        # Встановлюємо найстарший (most significant) і наймолодший (least significant) біти в 1:
        # - Найстарший біт в 1 забезпечує, що число дійсно має 'bits' бітів (тобто не менше за 2^(bits-1))
        # - Наймолодший біт в 1 гарантує непарність числа, оскільки всі парні числа (крім 2) складені
        candidate |= (1 << (bits - 1)) | 1

        # Виконуємо перевірку на простоту з допомогою тесту Міллера-Рабіна, задаючи 50 раундів перевірки
        if isPrimeRM(candidate, 50):
            return candidate  # Якщо число пройшло тест, воно ймовірно просте