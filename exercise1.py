# Второе дз

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

## Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def f1(num: int):
    multi = 1
    while num>0:
        multi = num * multi
        num -= 1
    return multi

numberN = InputValues('Enter number N: ')
listOfNumbers = [i+1 for i  in range(numberN)]
print(listOfNumbers)
listOfMulti = list(map(f1, listOfNumbers))
print(listOfMulti)

# Задайте список из n чисел последовательности (1 + 1/n)^n. и выведите на экран их сумму.

numberN = InputValues('Enter number N: ')
listOfNumbers = [(1 + 1/i)**i for i in range(1,numberN + 1)] 
print(listOfNumbers)
print(sum(listOfNumbers))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

numberN = InputValues('Enter number N: ')
listOfNumbers = [i for i in range(-numberN,numberN+1)]    #Задайте список из N элементов, заполненных числами из промежутка [-N, N].
print(listOfNumbers)
