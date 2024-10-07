import csv
import os

def openfile(path):
    if os.path.splitext(path)[1] == '.csv':
        print('Yep')
    else:
        print('Nope')