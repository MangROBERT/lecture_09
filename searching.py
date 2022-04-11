import os
import json
import numpy as np

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if (field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}):
        return None

    with open(file_path, "r") as soubor:
        slovniik = json.load(soubor)

    return slovniik[field]

# print(read_data("sequential.json", "unordered_numbers"))

def linear_search(my_sequence, hledane_cislo):
    slovnig = {"position" : [], "count" : 0}


    for i in range(0, len(my_sequence)):

        if int(my_sequence[i]) == int(hledane_cislo):
            slovnig["count"] += 1
            slovnig["position"].append(i)
        else:
            continue

    return slovnig

def pattern_search(the_sequence, vzor):
    neybytna = []

    for oi in range(0, len(the_sequence) - 3):
        if str(the_sequence[oi] + the_sequence[oi + 1] + the_sequence[oi + 2]) == str(vzor):
            neybytna.append(oi)
        else:
            continue

    neybytna_mnoz = set(neybytna)
    return neybytna_mnoz

def main():
    print(pattern_search(read_data("sequential.json", "dna_sequence"), "ATA"))
    pass


if __name__ == '__main__':
    main()