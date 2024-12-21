# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csvfile:
        # Используем DictReader для чтения CSV
        reader = csv.DictReader(csvfile)

        # Преобразуем каждую строку в словарь и собираем в список
        data = [OrderedDict(row) for row in reader]

    # Сериализуем в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
