"""
Практическое задание к уроку №1 курса "Базы данных и PyQt"
Студент: Максим Сапунов, Jenny6199@yandex.ru
Преподаватель: Илья Барбылев

Задача №3
Написать функцию host_range_ping_tab(), возможности
которой основаны на функции из примера 2. Но в данном случае результат должен быть
итоговым по всем ip-адресам, представленным в табличном формате.
Таблица должна состоять из двух колонок.
"""

from requests import head
from task_1 import host_ping
from task_2 import host_range_ping
from tabulate import tabulate


def host_range_ping_tab():
    host_dictionary = host_range_ping()
    print(tabulate([host_dictionary], headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == '__main__':
    host_range_ping_tab()