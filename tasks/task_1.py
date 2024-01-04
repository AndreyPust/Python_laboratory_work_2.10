#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*args):
    """
    Функция вычисления среднего геометрического всех переданных ей аргументов.
    В случае, если функции передается пустой список аргументов, она возвращает "None".
    """
    if args:
        composition = 1.0
        for i in args:
            composition *= i
        return round(pow(composition, 1 / len(args)), 2)
    else:
        return None


if __name__ == "__main__":
    # Необходимо разработать функцию, которая вычисляет среднее геометрическое всех
    # переданных ей аргументов a1, a2, a3, … , an. В случае, когда функции передается
    # пустой список аргументов, она должна возвращать значение «None».

    print(geometric_mean())
    print(geometric_mean(1, 2, 3, 4, 5))
    print(geometric_mean(1.1, 5.6, 8.9, 4, 3, 9.1))
