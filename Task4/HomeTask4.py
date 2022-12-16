# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
a1 = float(input('Введите первое число координаты точки А: '))
a2 = float(input('Введите второе число координаты точки А: '))
b1 = float(input('Введите первое число координаты точки B: '))
b2 = float(input('Введите второе число координаты точки B: '))
degree = 2

def DistanceAB():
    result = (b1 - a1)**degree + (b2 - a2)**degree
    abDistance = math.sqrt(result)
    abDistance = round(abDistance, 2)
    print(f'Расстояние между точками на оси координат = {abDistance}')
    return
print(DistanceAB())