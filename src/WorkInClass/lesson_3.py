_1 = lambda x: x+15
_2 = lambda x, y: print(x*y)

"""
Fibonachi lambda
"""
 
fim = lambda n: 1 if n <= 1 else fim(n-1)+fim(n-2)

"""
Reverse array
"""

list_revesre = lambda lst: [lst[i] for i in range(len(lst)-1, -1, -1)]
list_rev = lambda lst: lst[::-1]
mk = [1,2,3,4,5,6]
import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)
    return inner

@timer
def task_1(lst):
    n_lst = [lst[0]]
    for i in lst:
        if i not in lst:
            n_lst.append(i)
    return n_lst


def counter(func):
    count = 0

# functools itertools

#genenrators yeild

def gen(x):
    k = 0
    while x > k:
        yield k
        k += 1

def even_numbers():
    x = 2
    while True:
        yield x
        x += 2











