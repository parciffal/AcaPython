# Task 1
# Write a python programm which return given
# list without duplicates.

def tsak_1(lst):
    n_lst = [lst[0]]
    for i in lst:
        if i not in lst:
            n_lst.append(i)
    return n_lst

# Task 2
# Write a python program which return common
# elements of 2 lists.

def common_lists(lst1, lst2):
    common = []
    for i in ls:
        pass

# Task 3
# Write a python program which return elements
# which are in first list but not in second

# Task 4
# Write a python program which return elements
# are or in first list, either in second,
# but not in both

# Task 5
# Write a python program which return elements
# which are or in first, either in second,
# or in both

# Task 6
# Write  python function which get set
# and element value, and remove from set
# element with given value if exist



# Task 7
# Write a python python program,
# which return list from given set,
# where each element of list,
# is equal to cube of set element

def set_to_list(st):
    return [x**3 for x in st]

# Task 8
# Write a python program,
# which add a new value with given key in dict.

def dict_add(key, value, dct):
    dct[key] = value
    return dct

# Task 9
# Write a python program which concat 2 dicts.

def dict_concat(d1:dict, d2:dict):
    d = {**d1, **d2}
    return d

# Task 10
# Write a python program, which create a
# dictionary for given number N,
# where keys are numbers from 1 to N,
# and values are cubs of that numbers

def read_file(n, file_name):
    with open(file_name, 'r') as fi:
        #for i in range(n):
        #    print(fi.readline())
        fi.read()
        [print(fi.readline()) for x in range(n)]

read_file(2, 'test.txt')

def task_15(file_name):
    with open(file_name, 'r') as f:
        count = 0
        for line in f.readlines():
            line.replace(',', ' ')
            line.replace('.', ' ')
            line.replace(':', ' ')
            count+= len(line.split(' '))

    return count

print(task_15('test.txt'))

def task_14(file_name):
    with open(file_name, 'r') as f:
        max_word = f.read().replace(',', ' ').replace('.',' ').replace('\n', '').replace(':','').split(' ')
        max_word = sorted(max_word, key=len)[-1]
    return max_word

print(task_14('test.txt'))
            

