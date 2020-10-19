from sys import argv

script_name, salary_per_hour, work_time, bonus = argv


print("Имя скрипта: ", script_name)
print("Ставка в часах: ", salary_per_hour)
print("Выработка в часах ", work_time)
print("какой бонус у сотрудника: ", bonus)

print(f"Ваш сотрудник заработал за меясяц {int(salary_per_hour) * int(work_time) + int(bonus)}")
