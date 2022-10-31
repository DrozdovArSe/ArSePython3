#!/usr/bin/env python3
# coding=utf-8

import random

def random_array(n, m=8, max_value=21):
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)
        array.append(sub_array)
    return array

def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%5.1f\t" % j, end='')
        print()

def counting(array):
    print()
    indi = 0
    indj = 0
    max_value = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            e = array[i][j]
            if e > max_value:
                max_value = e
                indi = i
                indj = j
    print("Максимум: %d" % (max_value))
    print()
    return indi, indj

def main():
    rowCount = 4
    colCount = 5
    evens = 0
    array = random_array(rowCount, colCount)
    print("Условие задания:\n"
          "Подсчитать количество четных целых элементов,\n"
          "расположенных перед максимальным элементом таблицы \n"
          "и увеличить на это значение максимальный элемент")
    print_array(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)
            indi, indj = counting(array)
        elif key == '2':
            for i in range(rowCount):
                for j in range(colCount):
                    if i == indi and j == indj:
                        array[indi][indj] += evens
                    f = array[i][j]
                    moder = f%2
                    if moder == 0:
                        evens += 1
            print_array(array)
            break
        elif key == '3':
            exit(0)


if __name__ == '__main__':
    main()