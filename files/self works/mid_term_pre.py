# import json
# import re

# raw_cars = """
# - Продам Toyota Camry, 2018 г.в., цена 12500000 тг. Пробег 45000 км. Состояние идеал.
# - Срочно! BMW X5 (2020), 55000$, пробег 12000км, один владелец.
# - Audi A4 2015 года за 18000€. Контакты: 87071112233. Пробег 150000 км.
# """

# mark_pat = r"(\b[A-Z]\w+)"
# year_pat = r"\b\d{4}\b"
# price_pat = r"(\d+)\s*(?:\$|€|тг)"
# km_pat = r"(\d+)\s*км"

# x = re.findall(mark_pat,raw_cars)
# print(x[0] + " " + x[1])
# print(x[2] + " " + x[3])
# print(x[4] + " " + x[5])
# x = re.findall(year_pat,raw_cars)
# print(x)
# x = re.findall(price_pat,raw_cars)
# print(x)
# x = re.findall(km_pat,raw_cars)
# print(x)


# import re
# import json

# raw_cars = """
# - Продам Toyota Camry, 2018 г.в., цена 12500000 тг. Пробег 45000 км. Состояние идеал.
# - Срочно! BMW X5 (2020), 55000$, пробег 12000км, один владелец.
# - Audi A4 2015 года за 18000€. Контакты: 87071112233. Пробег 150000 км.
# """

# # Твои доработанные шаблоны
# mark_pat = r"[A-Z][a-zA-Z]+" # Ищем латиницу с большой буквы
# year_pat = r"\b\d{4}\b"
# price_pat = r"(\d+)\s*(?:\$|€|тг)" # Исправили ?: и добавили группу на число
# km_pat = r"(\d+)\s*км"

# results = []

# for line in raw_cars.strip().split('\n'):
#     mark = re.search(mark_pat, line)
#     year = re.search(year_pat, line)
#     price = re.search(price_pat, line)
#     km = re.search(km_pat, line)
    
#     results.append({
#         "brand": mark.group(0) if mark else "N/A",
#         "year": year.group(0) if year else "N/A",
#         "price": price.group(1) if price else "N/A", # Берем только цифры из группы 1
#         "mileage": km.group(1) if km else "N/A"
#     })

# print(json.dumps(results, ensure_ascii=False, indent=4))

# import json
# import re
# from datetime import datetime

# today = datetime(2024, 5, 20) 

# messages = [
#     "Подготовить отчет до 2024-05-25. Срочно!",
#     "Записаться к стоматологу (дедлайн: 2024-06-10), не забыть паспорт.",
#     "Проверить правки по проекту до 2024-05-18. Важно."
# ]

# results = []

# for line in messages:
#     task_pat = r"^([^()]+?)\s*(?:\(|до|дедлайн:)"
#     time_pat = r"\d{4}-\d{2}-\d{2}"
#     ts = re.search(task_pat, line)
#     tm = re.search(time_pat, line)
#     dt_tm = datetime.strptime(str(tm.group(0)),"%Y-%m-%d")
#     diff = dt_tm - today
    
    
#     results.append({
#         "Task" : ts.group(1).strip() if ts else "No date",
#         "Time left" : diff.days if tm else "No data"
#     })
# print(json.dumps(results, ensure_ascii=False, indent=4))

# from datetime import datetime

# text = "2026-02-01 2026-02-15 2026-03-20 2026-05-10"
# dates = text.strip().split()
# main_date = datetime.strptime(dates[0], "%Y-%m-%d")
# for i in range(1,len(dates)):
#     temp = datetime.strptime(dates[i],"%Y-%m-%d")
#     diff = abs(main_date - temp)
#     print(diff.days,end=" ")

# import json
# import re

# json_data = '{"Ivan": "123@gmail.com", "Serega": "lol_mail"}'
# data = json.loads(json_data)

# for name, email in data.items():
#     if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
#         print(name)

# from datetime import datetime
# semester = datetime.strptime(input(), "%Y-%m-%d")
# exam1 = datetime.strptime(input(), "%Y-%m-%d")
# exam2 = datetime.strptime(input(), "%Y-%m-%d")
# exam3 = datetime.strptime(input(), "%Y-%m-%d")

# print((exam1 - semester).days)
# print((exam2 - semester).days)
# print((exam3 - semester).days)

# import math

# a = float(input("Введите противолежащий катет (a): "))
# b = float(input("Введите прилежащий катет (b): "))

# # Используем atan2, передавая сначала "y" (противолежащий), потом "x" (прилежащий)
# res_rad = math.atan2(a, b)

# # Переводим в градусы
# res_deg = math.degrees(res_rad)

# print(f"Результат в радианах: {res_rad:.4f}")
# print(f"Результат в градусах: {res_deg:.2f}°")

import json

json_string = '{"name": "Иван", "age": 25, "is_client": true}'

# Превращаем строку в словарь (dict)
data = json.loads(json_string)

print(data["name"])  # Выведет: Иван
print(type(data))    # <class 'dict'>

pretty_json = json.dumps(
    data, 
    indent=4, 
    ensure_ascii=False, 
    sort_keys=True
)
print(pretty_json)