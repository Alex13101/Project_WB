import schedule
import time
import datetime
from def_extract_WB_grequests import search_right_product # импортируем Функцию для сбора данных и проверки цены по квери
from def_extract_WB_grequests import demonstration


search = input('что ищем? ')
# Функция для выполнения задачи по расписанию
def run_task():

    query = search  # Заменить на свои квери
    search_right_product(query)
    demonstration(search_right_product(query))
    print('Время проверки ', datetime.datetime.now())

# Запуск задачи по расписанию
schedule.every(2).minutes.do(run_task)  # Можно изменить интервал выполнения задачи

# Бесконечный цикл для выполнения задачи
while True:
    schedule.run_pending()
    time.sleep(1)
