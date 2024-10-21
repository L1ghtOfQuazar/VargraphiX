import csv
import os
from dataclasses import fields


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

def doublenormaliser(list):
    before, after, sh, s1, f  = list, [], 0, 0, []
    for i in before:
        if i not in after:
            after.append(i)
        else:
            f.append(i)
            after.append(i + str(f.count(i) + 1))
    return after


