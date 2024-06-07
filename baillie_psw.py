from rabin_miller import isPrimeRM
from lucas import lucas_test


def is_perfect_square(n):
    if n < 0:
        return False  
    if n == 0:
        return True  

    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2

    return x * x == n


def jacobi_symbol(n, k):
    assert k > 0 and k % 2 == 1  
    n %= k  # Зменшуємо n за модулем k
    t = 1
    while n != 0:
        while n % 2 == 0:
            n //= 2  # Відкидаємо всі множники 2 з n
            r = k % 8
            if r == 3 or r == 5:
                t = -t  # Змінюємо знак t, якщо r дорівнює 3 або 5
        n, k = k, n  # Міняємо місцями n і k
        if n % 4 == 3 and k % 4 == 3:
            t = -t  # Змінюємо знак t, якщо обидва n і k залишки 3 по модулю 4
        n %= k
    return t if k == 1 else 0  # Якщо k дорівнює 1, повертаємо t; інакше 0


def baillie_test(num):
    # Перелік відомих простих чисел для швидкої перевірки на дільність
    known_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
        211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
        283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
        379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
        461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541
    ]
    for known_prime in known_primes:
        if num == known_prime:
            return True  # Якщо число співпадає з відомим простим, повертаємо True
        elif num % known_prime == 0:
            return False  # Якщо число ділиться на відоме просте, повертаємо False

    if is_perfect_square(num):
        return False
    if not isPrimeRM(num, 2):
        return False  # Використовуємо тест Міллера-Рабіна для подальшої перевірки
    if not lucas_test(num):
        return False
    return True  # Якщо всі тести пройдено, num ймовірно просте

