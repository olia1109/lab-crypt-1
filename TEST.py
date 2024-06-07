import pytest
from rabin_miller import isPrimeRM as is_prime_rabin_miller
from baillie_psw import baillie_test as baillie_psw_test

# Тестові дані для перевірки простих чисел
PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 83813]
# Тестові дані для перевірки складених чисел, включаючи звичайні складені та числа Кармайкла
COMPOSITE_NUMBERS = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 10000000]
CARMICHAEL_NUMBERS = [561, 1105, 1729, 2465, 2821, 6601]


@pytest.mark.parametrize("number", PRIME_NUMBERS)
def test_miller_rabin_primes(number):
    """Тестуємо, чи правильно тест Міллера-Рабіна визначає прості числа"""
    assert is_prime_rabin_miller(number, 5) == True, f"Failed on prime {number}"


@pytest.mark.parametrize("number", COMPOSITE_NUMBERS + CARMICHAEL_NUMBERS)
def test_miller_rabin_composites(number):
    """Тестуємо, чи правильно тест Міллера-Рабіна визначає складені числа, включаючи числа Кармайкла"""
    assert is_prime_rabin_miller(number, 5) == False, f"Failed on composite {number}"


@pytest.mark.parametrize("number", PRIME_NUMBERS)
def test_baillie_psw_primes(number):
    """Тестуємо, чи правильно тест Бейлі-ПСВ визначає прості числа"""
    assert baillie_psw_test(number) == True, f"Failed on prime {number}"


@pytest.mark.parametrize("number", COMPOSITE_NUMBERS + CARMICHAEL_NUMBERS)
def test_baillie_psw_composites(number):
    """Тестуємо, чи правильно тест Бейлі-ПСВ визначає складені числа, включаючи числа Кармайкла"""
    assert baillie_psw_test(number) == False, f"Failed on composite {number}"


if __name__ == "__main__":
    pytest.main()
