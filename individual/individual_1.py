#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def first_sum_second(*args):
    """
    Функция вычисления суммы переданных ей аргументов, расположенных между первым и
    вторым положительными аргументами.
    В случае, если функции передается пустой список аргументов, она возвращает "None".
    """
    if args:
        positive_count = 0
        sum_args = float(0)
        count = 0

        for arg in args:
            if arg > 0:
                positive_count += 1

            if positive_count == 1 and args[count+1] > 0:
                break

            if positive_count == 1:
                sum_args += args[count+1]

            count += 1

        return sum_args

    else:
        return None


if __name__ == "__main__":
    # Необходимо найти сумму аргументов, расположенных между первым и вторым
    # положительными аргументами (Вариант 26 (8)). Если функции передается
    # пустой список аргументов, то она должна возвращать значение «None».

    print(first_sum_second())
    print(first_sum_second(10, -10, -20, -30, -50, 1))
    print(first_sum_second(-1, 10, -273, -3749, -372.1, -40, 1, 23, 50))
