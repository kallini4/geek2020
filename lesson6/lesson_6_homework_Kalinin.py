#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
#  и метод running (запуск). Атрибут реализовать как приватный.
#  В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#  Продолжительность первого состояния (красный) составляет 7 секунд,
#  второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#  Проверить работу примера, создав экземпляр и вызвав описанный метод.

# !! Хотел сделать, чтобы он был бесконечным, как светофор, но не смог придумать, как сделать
# чтобы время было разное, только с одинаковым интервалом получилось))) - time_running
# from time import sleep
# from itertools import cycle
#
# class TrafficLight:
#     __color = ["Red", "Yellow", "Green"]
#
#     def running(self):
#         i = 0
#         while i !=3:
#             print(TrafficLight.__color[i])
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1
#     def time_running(self):
#         for i in cycle(TrafficLight.__color):
#             print(i)
#             sleep(3)
#
#
# t = TrafficLight()
# t.running()
# t.time_running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# class Road:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         self.thickness = 5
#         self.weight = 25
#
#     def need_bitum(self):
#         bitum = self.length * self.width * self.thickness * self.weight
#         return (bitum)
#
#
# l = int(input("Insert road lenghth: "))
# w = int(input("Insert road width: "))
# r = Road(l,w)
# print(f"You need {r.need_bitum()} tons of bitum")

# 3  Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": int(wage), "bonus": int(bonus)}
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_ful_name(self):
#         print(f"Ваш работник: {self.name} {self.surname}")
#
#     def get_total_income(self):
#         income = self._income["wage"] + self._income["bonus"]
#         print(f"Ваш работник {name} {surname} имеет общий доход в {income} рублей")
#
#
# name = input("Введите имя Вашего сотудника ")
# surname = input("Введите фамилию Вашего сотудника ")
# position = input("Введите должность Вашего сотудника ")
# wage = int(input("Введите зарплату Вашего сотудника "))
# bonus = int(input("Введите премию Вашего сотудника "))
#
# worker_1 = Position(name, surname, position, wage, bonus)
# worker_1.get_ful_name()
# worker_1.get_total_income()

# 4 Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

# class Auto:
#
#     def __init__(self, name, speed, color, ispolice=False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.ispolice = ispolice
#
#     def auto_go (self):
#         print(self.name, "moved")
#
#     def auto_stop(self):
#         print(self.name, "stopped")
#
#     def auto_turn (self, direction):
#         print(f"{self.name} turned {direction}")
#
#     def auto_show_speed(self):
#         print(f"Speed of {self.name} is {self.speed}")
#
# class TownCar(Auto):
#     def auto_show_speed(self):
#         if self.speed > 60:
#             print(f"Your {self.name} speed is {self.speed}! You're overspeeding")
#         else:
#             print(f"Your {self.name} is moving at normal speed")
#
#
# class SportCar(Auto):
#     def auto_show_speed(self):
#         if self.speed < 100:
#             print(f"Your {self.name} is sportcar!! Move faster, man")
#         else:
#             print(f"Your {self.name} is moving at normal sportcar speed")
#
# class WorkCar(Auto):
#     def auto_show_speed(self):
#         if self.speed > 40:
#             print(f"Your {self.name} is overspeeding")
#         else:
#             print(f"Your {self.name} is moving at normal speed")
#
# class PoliceCar(Auto):
#     def is_police(self):
#         if not self.ispolice:
#             print(f"Your {self.name} car is fake police")
#         else:
#             print(f"Your {self.name} car is normal police")
#
# town_car = TownCar("Lada", 70, "black", False)
# town_car.auto_go()
# town_car.auto_stop()
# town_car.auto_turn("left")
# town_car.auto_show_speed()
# print(f"Your car {town_car.name} is police - {town_car.ispolice}")
#
# sport_car = SportCar("Aston Martin", 60, "gold", False)
# sport_car.auto_go()
# sport_car.auto_stop()
# sport_car.auto_turn("left")
# sport_car.auto_show_speed()
# print(f"Your car {sport_car.name} is police - {sport_car.ispolice}")
#
# work_car = WorkCar("Volvo", 60, "blue", False)
# work_car.auto_go()
# work_car.auto_stop()
# work_car.auto_turn("left")
# work_car.auto_show_speed()
# print(f"Your car {work_car.name} is police - {work_car.ispolice}")
#
# police_car = PoliceCar("Vaz-2112", 60, "blue", True )
# police_car.auto_go()
# police_car.auto_stop()
# police_car.auto_turn("left")
# police_car.auto_show_speed()
# police_car.is_police()


# 5 Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# # Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return "Draw start"
#
#
# class Pen(Stationery):
#
#     def draw(self):
#         return f"{self.title} draw start"
#
#
# class Pencil(Stationery):
#
#     def draw(self):
#         return f"{self.title} draw start"
#
#
# class Handle(Stationery):
#
#     def draw(self):
#         return f"{self.title} draw start"
#
#
# pen = Pen("синяя ручка")
# print(pen.draw())
#
# pencil = Pencil("простой карандаш")
# print(pencil.draw())
#
# handle = Handle("маркер перманентный")
# print(handle.draw())
