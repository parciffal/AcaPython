"""
TASK 1
Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։
"""

from typing import List


def task_1(first, second, n):
    return second + (n-2)*(second-first)

"""
TASK 2
CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
որոնք հայտնվում են տվյալ մուտքագրում:
Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
հայտնված թվերի գումարը։
"""

def task_2(inp_str:str):
    count = 0
    for i in inp_str.split(" "):
        if i.isnumeric():
            count += int(i)
    return count
    

"""
TASK 3
Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարաflag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1կflag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1
    i += 1
դեփքում:
Օրինակ՝
input: [1,2,3], [1,3,2], [5,0,-4]
output: Sorted, Unsorted, Sorted
"""
def task_3(arr):
    checked_mec = True
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            checked_mec = True
        else:
            checked_mec = False
            break
    checked_poqr = True
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            checked_poqr = True
        else:
            checked_poqr = False
            break
    if checked_poqr == True or checked_mec == True:
        return 'Sorted'
    else:
        return 'Unsorted'


"""
TASK 4
Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
կատարյալ թիվ է, թե ոչ։
Հ․Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների
գումարին։
Օրինակ՝
6 ի բաժանարարներն են 1, 2 և 3 , 1 + 2 + 3 = 6, կատարյալ է 12֊ի բաժանարարներըն
են 1, 2 , 3 , 4 , 6 , 1 + 2 + 3 + 4 + 6 = 16, հետևաբար
կատարյալ չէ։
"""


def task_4(n):
    sd = [] 
    for i in range(1, n//2+1):
        if n%i == 0:
            sd.append(i)
    count = 0
    for i in sd:
        count += i
    if count == n:
        return 'Kataryal'
    else:
        return 'Voch Kataryal'

"""
TASK 5
Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
էլեմենտների գումարը։
"""

def task_5(arr):
    count = arr[0]
    for i in arr[1:]:
        count+=i
    return count

"""
TASK 6
Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
ցուցակի ամենամեծ էլեմենտը։
"""

def task_6(arr):
    max = arr[0]
    for i in arr[1:]:
        if i > max:
            max = i
    return max


"""
TASK 7
Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
էլեմենտները։
"""
def task_7(arr, ke):
    for i in range(0, len(arr)):
        if arr[i] == ke:
            arr.pop(i)
    return arr

print(task_7([2,4,2,2,3,13,4,24], 2))


"""
TASK 8
Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
էլեմենտների արտադրյալը։
"""

