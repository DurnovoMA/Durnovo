import json

def task(FILE) -> float:
    with open(FILE) as f:
        json_data = json.load(f)
        summa = round(sum(i["score"] * i["weight"] for i in json_data),3)
    return summa

relative_path = "input.json"
print(task(relative_path))
