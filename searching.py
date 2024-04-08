import json
import os
import json

template = "GA"
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    with open(file_name) as data_file:
        data = json.load(data_file)
    for i in data[2]:
        



def main():
    pass


if __name__ == '__main__':
    main()