import pandas as pd
import csv

def count_csv_lines(path):
    length = 0
    with open(path) as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            length += 1
    return length

def save_as_csv(thing_to_save, filename: str):
    thing_types = [list, pd.core.frame.DataFrame]
    if type(thing_to_save) not in thing_types:
        raise AttributeError(f'{thing_to_save} is an invalid thing. Valid things are lists and dataframes')
    
    filename = f'{filename}.csv'
    with open(filename, 'w') as file:
        if type(thing_to_save) == list:
            for row in thing_to_save:
                file.write(f'{row}\n')
        if type(thing_to_save) == pd.core.frame.DataFrame:
            thing_to_save.to_csv(file, index=False, header=False)

def strip_bounded(string: str, par=True, bra=True):
    s = string
    if par:
        offender = s[s.find(f'('):s.find(f')')+1]
        s = s[0:s.index(offender)] + s[s.index(offender) + len(offender):]
    if bra:  
        offender = s[s.find(f'['):s.find(f']')+1]
        s = s[0:s.index(offender)] + s[s.index(offender) + len(offender):]  
    return s