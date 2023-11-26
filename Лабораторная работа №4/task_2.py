# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(input_file, output_file) -> None:
    with open(input_file) as fi:
        dict_csv = [line for line in csv.DictReader(fi, delimiter=",")]

    with open(output_file, "w") as fo:
        json.dump(dict_csv, fo, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME,OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
