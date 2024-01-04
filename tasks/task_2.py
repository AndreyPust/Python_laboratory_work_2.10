#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean(*args):
    """
    Функция вычисления среднего гармонического всех переданных ей аргументов.
    В случае, если функции передается пустой список аргументов, она возвращает "None".
    """
    if args:
        harmonic = 0
        for i in args:
            harmonic += 1 / i
        return round(len(args) / harmonic, 2)
    else:
        return None


if __name__ == "__main__":
    # Необходимо написать функцию, вычисляющую среднее гармоническое переданных
    # ей аргументов a1, a2, a3, … , an. В случае, когда функции передается пустой
    # список аргументов, она должна возвращать значение «None».

    print(harmonic_mean())
    print(harmonic_mean(1, 2, 3, 4, 5))
    print(harmonic_mean(1.1, 5.6, 8.9, 4, 3, 9.1))
