import csv

def load_table(x, get_column_types=False):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        fl = list(rows)
        print(fl)
    if get_column_types == True:
            ln = len(fl)
            flag_3 = 0
            dc = {}
            print(ln)
            flag_2 = 1
            for tp in range(ln):
                print(tp)
                row_1 = fl[flag_3]
                row_1 = row_1[0].split(';')
                li = {}
                flag = 0
                for i in row_1:
                    try:
                        if i == 'True' or i == 'False':
                            flag += 1
                            li.update({flag: 'bool'})
                        elif '.' in i:
                            if float(i):
                                flag += 1
                                li.update({flag: 'float'})
                        elif int(i):
                            flag += 1
                            li.update({flag: 'int'})
                        else:    
                            flag += 1
                            li.update({flag: 'str'})
                    except ValueError:
                        flag += 1
                        li.update({flag: 'str'})
                flag_3 += 1
                dc.update({flag_2: li})
                flag_2 += 1
            return dc
    return fl

def print_table(x):
    with open(f'{x}.csv', 'r') as fl:
        lines = csv.reader(fl)
        for i in lines:
            print(f'[{';'.join(i)}]')

def save_table(x):
    with open(f'{x}.csv', 'r') as fl:
        lines = csv.reader(fl)
        with open(f'{x}.txt', 'w') as ft:
            for i in lines:
                for el in i:
                    ft.write(f'[{el}]')
                ft.write('\n')


def get_rows_by_number(x, start, stop, copy_table=False):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        flag = start
        n_rows = []
        for i in rows:
            if flag == stop+1:
                break
            else:
                n_rows.append(i)
            flag += 1
    if copy_table == True:
        with open(f'{x}_2.csv', 'w') as fl2:
            file_csv = csv.writer(fl2, delimiter=';', lineterminator='\r')
            file_csv.writerows(n_rows)
    return n_rows

def get_rows_by_index(x,*args, copy_table=False):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        li = list(args)
        n_rows = []
        for i in rows:
            for el in li:
                try:
                    i_2 = i[0].split(';')
                    if type(el)(i_2[0]) == el:
                        n_rows.append(i)
                        continue
                except ValueError:
                    continue
    if copy_table == True:
        with open(f'{x}_2.csv', 'w') as fl2:
            file_csv = csv.writer(fl2, delimiter=';', lineterminator='\r')
            file_csv.writerows(n_rows)
    n_rows = n_rows[::-1]
    return n_rows
                
def get_column_types(x, by_number=True):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        header = next(rows)
        row_1 = next(rows)
        row_1 = row_1[0].split(';')
        li = {}
        flag = 0
        for i in row_1:
            try:
                if i == 'True' or i == 'False':
                    flag += 1
                    li.update({flag: 'bool'})
                elif '.' in i:
                    if float(i):
                        flag += 1
                        li.update({flag: 'float'})
                elif int(i):
                    flag += 1
                    li.update({flag: 'int'})
                else:    
                    flag += 1
                    li.update({flag: 'str'})
            except ValueError:
                flag += 1
                li.update({flag: 'str'})
    return li
        
def set_column_types(x, column, types_dict, by_number=True):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        header = next(rows)
        row_1 = next(rows)
        row_1 = row_1[0].split(';')
        li = {}
        flag = 0
        for i in row_1:
            if flag == column:
                li.update({flag: f'{types_dict}'})
                flag += 1
            try:
                if i == 'True' or i == 'False':
                    flag += 1
                    li.update({flag: 'bool'})
                elif '.' in i:
                    if float(i):
                        flag += 1
                        li.update({flag: 'float'})
                elif int(i):
                    flag += 1
                    li.update({flag: 'int'})
                else:    
                    flag += 1
                    li.update({flag: 'str'})
            except ValueError:
                flag += 1
                li.update({flag: 'str'})
    return li

def get_values(x, column=1):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        header = next(fl)
        header = (''.join(header)).split(';')
        li = [column]
        if type(column) != int:
            column = header.index(column)+1
        flag = 1
        for i in rows:
            i = (''.join(i)).split(';')
            for el in i:
                if flag == column:
                    li.append(el)
                flag += 1
            flag = 1
        return li

def get_value(x, column=1):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        header = next(fl)
        header = (''.join(header)).split(';')
        li = [str(column)]
        if type(column) != int:
            column = header.index(column)+1
        flag = 1
        for i in rows:
            i = (''.join(i)).split(';')
            for el in i:
                if flag == column:
                    li.append(el)
                flag += 1
            flag = 1
        with open(f'{x}_2.csv', 'w') as fl2:
                file_csv = csv.writer(fl2, delimiter=';', lineterminator='\r')
                file_csv.writerow(li)
        return ';'.join(li)
    
def set_values(x, values, column=0):
    with open(f'{x}.csv', 'r') as fl:
        rows = csv.reader(fl)
        header = next(rows)
        flag = 1
        li = [header]
        flag_2 = 0
        for i in rows:
            print(i)
            for el in range(len(i)):
                if flag == column:
                    i[el] = values[flag_2]
                    li.append(i)
                    print(li)
                    flag_2 += 1
                flag += 1
            flag = 1
            if flag_2 > len(list(rows)):
                break
        with open(f'{x}.csv', 'w') as fw:
            csv_writer = csv.writer(fw, lineterminator='\r')
            csv_writer.writerows(li)

import pickle

def load_pickle(x):
    objects = []
    with (open(f"{x}.dat", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

def save_table(x, a):
    with open(f'{x}.dat', 'wb') as dump_out:
        pickle.dump(a, dump_out)