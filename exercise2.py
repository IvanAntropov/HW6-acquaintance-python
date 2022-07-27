# Третье дз

import random

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def SumaOfNumbers(ListN: list):
    index = 1
    suma = 0
    while index < len(ListN):
        suma += ListN[index]
        index += 2
    return suma

numberN = InputValues('Enter number N: ')
listOfNumber = [random.randint(1,100) for i in range(numberN)] 
print(f'List: {listOfNumber}')
print(f'Sum of numbers: {SumaOfNumbers(listOfNumber)}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

listOfNumber2 = [i for i in range(1,11)] 
listOfMulti = [listOfNumber2[i] *(listOfNumber2[len(listOfNumber2) - 1 - i]) for i in range(int(len(listOfNumber2)/2))]
print(listOfNumber2)
print(listOfMulti)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def f1(x):
    if x in(1,2):
        return 1
    return f1(x - 1) + f1(x - 2)

numberN = InputValues('Enter number N: ')
listOfNumber3 = [i for i in range(1,numberN+1) if i != 0] 
listFibonachi = list(map(f1,listOfNumber3))
print(listFibonachi) # правда без отрицательных индексов




