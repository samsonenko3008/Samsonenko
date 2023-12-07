# TODO решите задачу


import csv
import json

input_file = "input.csv"
output_file = "output.json"

def task():
    with open(input_file) as c:
        reader = csv.DictReader(c, delimiter=",", quotechar="\n")
        row = list(reader)

    with open(output_file, "w") as f:
        json.dump(row, f, indent=4)
task()

with open(output_file) as output:
    for line in output:
        print(line, end="")




