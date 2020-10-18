# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#
# def division(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'No Zero Division'
#     except ValueError:
#         return 'value incorect'
#     finally:
#         print("Thanks a lot")
#
#
# print("Your result is: ", division((int(input('Enter first number: '))), (int(input('Enter second number: ')))))

# 2 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# def user_info(*args):
#     return list(args)
#
#
# a = list(user_info(input('Enter name: '), input('Enter second name: '),
#                    input('Enter birth day: '),input('Enter live town: '),
#                    input('Enter email: '), input('Enter tel number: ')))
#
# for i in enumerate(a, 1):
#     print(i)


# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# def my_func():
#     z = [int(input("Insert first number: ")), int(input("Insert second number: ")),
#          int(input("Insert third number: "))]
#     z.remove(min(z))
#     return sum(z)
#
#
# print(my_func())


# 4 Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# def my_func(x, y):
#     try:
#         return 1 / x ** abs(y)
#     except ZeroDivisionError:
#         return 'No Zero Division'
#     except ValueError:
#         return 'value incorect'
#
#
# x = int(input("ВВедите действительное положительное число: "))
# y = int(input("ВВедите действительное отрицательное число: "))
# if x <= 0:
#     x = int(input("ВВедите действительное положительное число: "))
# else:
#     print(my_func(x, y))
# if y >= 0:
#     y = int(input("ВВедите действительное отрицательное число: "))
# else:
#     print(my_func(x, y))


#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


# def int_func(st):
#     return ' '.join(x.capitalize() for x in st.split())
# 
# # word = input("Insert an english word:")
# # print(int_func(word))
# 
# def capital_string(st):
#     list = st.split(' ')
#     new_list = []
#     for el in list:
#         new_list.append(int_func(el))
#         my_string = ', '.join(new_list)
#     return(my_string)
# 
# string = input("Insert an english sentence:")
# print(capital_string(string))
