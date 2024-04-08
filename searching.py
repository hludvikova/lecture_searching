import json
import os
import json
from typing import List, Any

template = ["G", "A"]
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    middle_char=[]
    with open(file_name) as data_file:
        data = json.load(data_file)
    i=0
    for i in data[2]:
        if i == template[0]:
            i+=1
            if i == template[1]:
                x = int(len(data[2])/2)
                if len(data[2])%2!=0:
                    return middle_char.append(data[x])
                else:
                    return middle_char.append(data[2][x-1:x+1])
            else:
                continue
        else:
            continue
    return middle_char

def pattern_search(seq, pattern):
    positions = set()
    pattern_length = len(pattern)
    for i in range(len(seq)):
        if seq[i:i+pattern_length] == pattern:
            positions.add(i)
    return positions


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid + 1
        elif numbers[mid] > target:
            high = mid - 1
        else:
            return mid
    return None

def main():
    with open('sequential.json', 'r') as f:
        data = json.load(f)
    numbers = data['ordered_numbers']
    target = 42  # Zde můžete definovat hledané číslo
    result = binary_search(numbers, target)
    print(f'Index of {target}: {result}')

if __name__ == '__main__':
    main()



if __name__ == '__main__':
    main()