# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# zero = 0
#
# for i in range(1, 6):
#     print(i, ") ", zero, sep="")
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# i = 0
# quant = 0
#
# while i < 10:
#     number = int(input("Введите число: "))
#     if number == 5:
#         quant += 1
#     i += 1
#
# print("Количество введеных 5:", quant)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1, 101):
#     sum += i
#
# print(sum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# multiptication = 1
#
# for i in range(1,11):
#     multiptication *= i
#     i += 1
#
# print("Произведение чисел от 1 до 10:", multiptication)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
# integer_number = 2129
#
# while integer_number > 0:
#     print(integer_number % 10)
#     integer_number = integer_number // 10
'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 3941
# sum = 0
#
# while integer_number > 0:
#     sum += integer_number % 10
#     integer_number = integer_number // 10
#
# print(sum)
'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 4912
# quant = 1
#
# while integer_number > 0:
#     quant *= integer_number % 10
#     integer_number = integer_number // 10
#
# print("Произведение цифр числа:", quant)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 2352
#
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Да')
#         break
#     integer_number = integer_number // 10
# else:
#     print('Нет')
'''
Задача 9
Найти максимальную цифру в числе
'''
# integer_number = 2137
# max = 0
#
# while integer_number>0:
#     figure = integer_number%10
#     if max < figure:
#         max = figure
#     integer_number = integer_number//10
#
# print("Максимальная цифра в числе:",max)
'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = 75935
# quant = 0
#
# while integer_number > 0:
#     figure = integer_number % 10
#     if figure == 5:
#         quant += 1
#     integer_number = integer_number // 10
#
# print("Количество цифр 5 в числе:", quant)
