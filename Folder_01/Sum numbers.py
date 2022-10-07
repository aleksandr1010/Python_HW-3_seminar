# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint

def get_list(n, first, last):
    return [randint(first, last) for i in range(n)]

def sum_odd_position(list):
    return sum(list[1::2])

n = 15
first = 1
last = 15

list = get_list(n, first, last)
print(list)
print(sum_odd_position(list))