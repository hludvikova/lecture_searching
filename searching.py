import json
import os
import json

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
    save=[]
    with open(file_name) as data_file:
        data = json.load(data_file)
    i=0
    for i in data[2]:
        if i == template[0]:
            i+=1
            if i == template[1]:
                x = int(len(data[2])/2)
                if len(data[2])%2!=0:
                    save.append(data[x])
                else:
                    continue
            else:
                continue
        else:
            continue
    i += 1




def main():
    pass


if __name__ == '__main__':
    main()