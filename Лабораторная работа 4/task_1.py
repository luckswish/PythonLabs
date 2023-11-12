import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    sum_values = sum(item["score"] * item["weight"] for item in data)
    return round(sum_values, 3)


if __name__ == '__main__':
    print(task())

