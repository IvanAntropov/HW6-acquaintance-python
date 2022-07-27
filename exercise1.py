# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

# def MultiOfNumbers(num: int):
#     multi = 1
#     listOfMulti = []
#     for i in range(num):
#         multi = multi*(i + 1)
#         listOfMulti.append(multi)
#     defString = f'A set of multi of numbers from 1 to {num} is {listOfMulti}'
#     return defString

# numberN = InputValues('Enter number N: ')
# print(MultiOfNumbers(numberN))

# ------------------------------------------------------------------------------

def f(num: int):
    multi = 1
    while num>0:
        multi = num * multi
        num -= 1
    return multi

numberN = InputValues('Enter number N: ')
listOfNumbers = [i+1 for i  in range(numberN)]
print(listOfNumbers)
listOfMulti = list(map(f, listOfNumbers))
print(listOfMulti)
