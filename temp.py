import math

# Спросим, что хорошего в этой библиотеке.
# print(math.__doc__)
print(print.__doc__)
# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard.


# для задания из практикума
from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
          'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float):
    if your_number<=0:
        return 0
    print('Мы вычислили квадратный корень из введённого вами '
          f'числа. Это будет: {CalculateSquareRoot(your_number)}')


calc(25.5)