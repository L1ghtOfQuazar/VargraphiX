import csv
import os
from dataclasses import fields


def openfile(path):
    if os.path.splitext(path)[1] == '.csv':
        print('Yep')
        print(''.join(os.path.splitext(path)))
    else:
        print('Nope')

def data_reading(path):
    fullpath = str(''.join(os.path.splitext(path)))
    fields, rows = [], []
    with open(fullpath, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file, delimiter=",")
        # creating a csv reader object
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        print(fields)
        print(rows)
        print(len(fields)) #cтолбцы
        print(len(rows)) #cтроки не считая заголовка
        return len(fields), len(rows), fields, rows


def fieldnamenormaliser(list):
    fields, fieldsn  = list, []
    for i in fields:
        if '_' not in i:
            fieldsn.append(i.title())
        else:
            n = ' '.join(i.split('_')).title()
            fieldsn.append(n)
    return fieldsn
