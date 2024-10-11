import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):  # Основна функція-генератор
    numbers = re.findall(r'\d+\.\d+', text)
    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable):  # Функція для підрахунку сумми
    return sum(func(text))


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")