# 1 Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 'text', 2.01, False]
print(my_list)
my_list.append("xyz")
print(my_list)
list = [29, [1, 2], True]
my_list.extend(list)
print(my_list)
my_list.insert(1, "hi")
my_list.insert(-1, "True")
print(my_list)
my_list.remove("True")
my_list.remove("hi")
print(my_list)
my_list.pop(0)
print(my_list)
print(my_list.index("text"))
my_list.reverse()
print(my_list)
print(my_list.index('text'))
print(len(my_list))
ind = 0
while ind < len(my_list):
    print(type(my_list[ind]))
    ind += 1

my_list = list(input("Insert word"))
num = int(input("Insert number"))
my_list.append(num)
print(my_list)
ind = 0
while ind < len(my_list):
    print(type(my_list[ind]))
    ind += 1

# 2 Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
my_list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    el = (input())
    my_list.append(el)
print("Your list is", my_list)
ind = 0
new_ind = 1
while ind < len(my_list) and new_ind < len(my_list):
    my_list[ind], my_list[new_ind] = my_list[new_ind], my_list[ind]
    ind += 2
    new_ind += 2
print(my_list)

# 3Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
m = int(input("Insert month number"))
while m > 12:
    m = int(input("Insert normal month number (1-12)"))
if 3 <= m <= 5:
    print("It's spring")
elif 6 <= m <= 8:
    print("It's summer")
elif 9 <= m <= 11:
    print("It's autumn")
else:
    print("It's winter")

m = int(input("Insert month number"))
year_dict = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
             9: "Autumn", 10: "Summer", 11: "Summer", 12: "Winter"}
while 0 >= m or m > 12:
    m = int(input("Insert month number (1-12"))
print("Your month is part of", year_dict.get(m))

# 4 Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.
n = input("Insert any sentence ")
new_list = n.split(' ')
for i in new_list:
    if len(i) > 10:
        print(i[1:11])
    else:
        print(i)

n = input("Insert any sentence ")
new_list = n.split(' ')
for i in enumerate(new_list, 1):
    if len(i) > 10:
        print(i[1:11])
    else:
        print(i)

# 5 Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
new_num = int(input("Insert any number "))
my_list.append(new_num)
a = sorted(my_list, reverse=True)
print(a)
