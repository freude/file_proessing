import os
import numpy as np


directory = './'
counter = 0

dictionaries = {}

for filename in os.listdir(directory):
    d = {}
    if filename.endswith(".dat"):
        counter += 1
        with open(filename, 'r') as f:
            for line in f:
                splited_line = line.split()

                if len(splited_line) > 0:
                    if len(splited_line) > 1:
                        d[splited_line[0]] = int(splited_line[1])
                    else:
                        d[splited_line[0]] = None

        dictionaries[int(''.join([s for s in list(filename) if s.isdigit()]))] = d

num_of_xs = 500
table = np.empty((num_of_xs-1, counter-1)) * np.nan

keys = dictionaries[1].keys()

for j1, key in enumerate(keys):
    for j2 in range(counter-1):
        if key in dictionaries[j2+2]:
            table[j1, j2] = dictionaries[j2+2][key]

# print(table[:10,:])

table_txt = ""

for j, key in enumerate(keys):

    table_txt += key + " " + str(table[j])[1: -1] + '\n'


print(table_txt)


