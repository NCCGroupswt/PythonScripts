import sys
import os
from itertools import izip_longest

fileName = sys.argv[1]

def grouper(n, iterable, fillvalue = None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = input('Please enter how many lines per file: ')

fileDir = "Split_" + fileName

with open(fileName) as f:
    os.makedirs(fileDir)
    os.chdir(fileDir)
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        newFileName = fileName + "_" + str(i) + ".log"
        with open(newFileName, 'w') as fout:
            fout.writelines(g)
