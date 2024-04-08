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




def pattern_search(seq, template):
    middle_char=[]
    with open("sequential.json") as data_file:
        data = json.load(data_file)
    i=0

    if "dna_sequence" in data:
        print("Key exist in JSON data")
        for dna_sequence in data:
            if i == template[0]:
                i+=1
                if i == template[1]:
                    x = int(len(data[2])/2)

                else:
                    continue
            else:
                continue
    else:
        print("Key doesn't exist in JSON data")
        middle_char

    return middle_char




def main():
    pass


if __name__ == '__main__':
    main()