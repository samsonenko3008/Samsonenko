# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    with open(INPUT_FILENAME) as c:
        reader = csv.DictReader(c, delimiter=",", quotechar="\n")
        row = list(reader)  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(row, f, indent=4)  # TODO Сериализовать в файл с отступами равными 4



task()

with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
        print(line, end="")
