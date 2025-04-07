import json
import os

# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data[field]


def linear_search(seq, number):
    positions = []
    for index, value in enumerate(seq):
        if value == number:
            positions.append(index)

    return {
        "positions": positions,
        "count": len(positions)
    }


def main():
    file_name = "sequential.json"
    field = "unordered_numbers"
    seq = read_data(file_name, field)
    if seq is None:
        print("Chybný název pole nebo soubor.")
        return

    number_to_find = 7  # ← zadej číslo, které chceš hledat
    result = linear_search(seq, number_to_find)

    print(f"Výsledky hledání čísla {number_to_find}:")
    print(f"Pozice: {result['positions']}")
    print(f"Počet výskytů: {result['count']}")


if __name__ == '__main__':
    main()
