"""
TASK 1
Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։
"""

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
Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, 
եթե թվերը նշված են ոչ աճող կամ չնվազող հերթականությամբ, 
իսկ «Չտեսակավորված» հակարաflag = 0 դեփքում:
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
    while ke in arr:
        arr.remove(ke)
    return arr

"""
TASK 8
Գրեք ֆունկցիա որը կվերադարձնի տրված 
թվային արժեքներով ցուցակի բոլոր
էլեմենտների արտադրյալը։
"""

def task_8(arr):
    count = arr[0]
    for i in arr[1:]:
        count *= i
    return count
"""
TASK 9
Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
բազմապատիկ է։
"""
def task_9(tox: str):
    new_tox = ''
    if len(tox)%4 == 0:
        for i in range(len(tox)-1,-1,-1):
            new_tox += tox[i]
    if new_tox == '':
        return tox
    else:
        return new_tox

"""
TASK 10
Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։
"""
def task_10_rec(index):
    if index == 0 or index == 1:
        return index
    return task_10_rec(index-1) + task_10_rec(index-2)


def task_10_iter(index):
    count = 0
    if index == 0 or index == 1:
        return index
    first = 0
    second = 1
    while count < index:
        nxt = first + second
        first, second = second, nxt
        count += 1
    return first

"""
TASK 11
Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
ամենափոքր ընդհանուր բազմապատիկը։
"""

def task_11(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


"""
TASK 12
Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է
"""
def task_12(n):
    found = True
    while found:
        temp = n
        rev = 0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        if temp == rev:
            found = False
            return temp
        else:
            n = temp+1

"""
TASK 13
Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։
"""


def task_13(N:str, x = 0, y = 0):
    """
        To hold several steps need to save 
        cordinates not in function
    """
    if N.lower() == 'up':
        y += 1
    elif N.lower() == 'down':
        y -= 1
    elif N.lower() == 'right':
        x += 1
    elif N.lower() == 'left':
        x -= 1
    return (x,y)

"""
TASK 14
Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:
Օրինակ
Ցուցակ1 = [1,2,3,4,5,6]
Ցուցակ2 = [6,1,2,3,4,5]
Վերադարձել True
"""

def task_14(arr_1, arr_2):
    if arr_1[-1] == arr_2[0] or arr_1[0] == arr_2[-1]:
        for i in range(1, len(arr_1)-1):
            if arr_1[i] != arr_2[i+1] or arr_1[i+1] != arr_2[i]:
                break
        return True
    else:
        return False

"""
TASK 15
Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:
Օրինակ՝
● For n = 152, the output should be
deleteDigit(n) = 52;
● For n = 1001, the output should be
deleteDigit(n) = 101.
"""

def task_15(n):
    str_n = [*str(n)]
    nums = []
    for i in range(len(str_n)):
        new_n = [*str_n]
        new_n.pop(i)
        num = ''
        for i in new_n:
            num += i
        nums.append(int(num))
    max = nums[0]
    for i in nums[1:]:
        if max < i:
            max = i
    return max

"""
TASK 16
Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
բաղկացած միայն առաջին tuple֊ի թվերից։
"""

def task_16(tpl:tuple):
    lst = []
    for i in tpl:
        if isinstance(i, int) or isinstance(i, float):
            lst.append(i)
    ntpl = tuple(lst)
    return ntpl

"""
TASK 17
Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
է ստացած արժեքը tuple մեջ։
"""

def tpl_append(tpl, value):
    return (*tpl, value)

"""
TASK 18
Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։
"""

def tuple_to_list(tpl):
    sr = ''
    for i in range(len(tpl)):
        if i == len(tpl)-1:
            sr += tpl[i]
        else:
            sr += tpl[i] + '-'
    return sr

"""
TASK 19

Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
len() ֆունկցիա֊ի օգտագորձմամբ։
"""

def length(lst):
    count = 0
    for _ in lst:
        count+=1

    return count

"""
TASK 20
Ticket numbers usually consist of an even number of digits. A ticket number is considered
lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it&#39;s lucky or not. Not using: string, list, tuple, set
types.
Example:
For n = 1230, the output should be:
is_lucky(n) = True;
For n = 239017, the output should be
is_lucky(n) = False.
"""

def get_len(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def get_num(index, n)-> int:
    for  i in range(index):
        n //= 10
    return int(n%10)

def task_20(n: int):
    first = 0
    second = 0
    end = get_len(n)-1
    lnmid = int(get_len(n)/2) 
    for i in range(0, lnmid):
        second += get_num(end, n)
        first += get_num(i, n)
        end -= 1
    if second == first:
        return True
    return False

"""
TASK 21
Euler function is return a count of numbers not great than N, which are mutualy simple with
N.
Example φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function
which return count of numbers mutually simple with given N.
"""

def maxBaj(a,b):
    max, min =(a,b) if a>b else (b,a)

    if max%min == 0:
        return min
    else:
        for i in range(min//2+1, 1, -1):
            if max%i==0 and min%i==0:
                return i
    return 1

def task_21(n): 
    count = 1
    for i in range(2, n):
        if (maxBaj(i, n) == 1):
            count += 1
    return count

"""
TASK 22 *
You are given a 0-indexed string array words, where words[i] consists of lowercase English
letters. In one operation, select any index i such that 0 &lt; i &lt; words.length and words[i - 1]
and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
as long as you can select an index that satisfies the conditions.
Return words after performing all operations. It can be shown that selecting the indices for
each operation in any arbitrary order will lead to the same result.
An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase using all the original letters exactly once. For example, &quot;dacb&quot; is an anagram of
&quot;abdc&quot;.
Example:
Input: words = [&quot;abba&quot;,&quot;baba&quot;,&quot;bbaa&quot;,&quot;cd&quot;,&quot;cd&quot;]
Output: [&quot;abba&quot;,&quot;cd&quot;]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = &quot;bbaa&quot; and words[1] = &quot;baba&quot; are anagrams, we choose index 2 and
delete words[2].
Now words = [&quot;abba&quot;,&quot;baba&quot;,&quot;cd&quot;,&quot;cd&quot;].
- Since words[1] = &quot;baba&quot; and words[0] = &quot;abba&quot; are anagrams, we choose index 1 and
delete words[1].
Now words = [&quot;abba&quot;,&quot;cd&quot;,&quot;cd&quot;].
- Since words[2] = &quot;cd&quot; and words[1] = &quot;cd&quot; are anagrams, we choose index 2 and delete
words[2].
Now words = [&quot;abba&quot;,&quot;cd&quot;].
We can no longer perform any operations, so [&quot;abba&quot;,&quot;cd&quot;] is the final answer.

Example 2:
Input: words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;,&quot;e&quot;]
Output: [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;,&quot;e&quot;]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are
performed.
Constraints:
1) 1 &lt;= words.length &lt;= 100
2) 1 &lt;= words[i].length &lt;= 10
3) words[i] consists of lowercase English letters.

"""

def sort_chars(word):
    chars  = {}

    for ch in word:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    return chars

def task_22(words: list):
    i = 0
    while i < len(words) - 1:
        if sort_chars(words[i]) == sort_chars(words[i + 1]):
            words.remove(words[i + 1])
            continue
        i += 1
    return words
"""
TASK 23 **
You are given an array of strings names, and an array heights that consists of distinct
positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
denote the name and height of the ith person. Return names sorted in descending
order by the people&#39;s heights.
Example 1:
EInput: names = [&quot;Mary&quot;,&quot;John&quot;,&quot;Emma&quot;], heights = [180,165,170]
Output: [&quot;Mary&quot;,&quot;Emma&quot;,&quot;John&quot;]
Explanation: Mary is the tallest, followed by Emma and John.
xample 2:
Input: names = [&quot;Alice&quot;,&quot;Bob&quot;,&quot;Bob&quot;], heights = [155,185,150]
Output: [&quot;Bob&quot;,&quot;Alice&quot;,&quot;Bob&quot;]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
Constraints:
1) n == names.length == heights.length
2) 1 <= n <= 10^3
3) 1 <= names[i].length <= 20
4) 1 <= heights[i] <= 10^5
5) names[i] consists of lower and upper case Engl:ish letters.
6) All the values of heights are distinct.
"""

def task_23(names: list, heights: list):
    comp = []
    for i in range(len(names)):
        comp.append([names[i], heights[i]])
    comp = sorted(comp, key=lambda x:x[1], reverse=True)
    comp = [x[0] for x in comp]
    return comp

"""
TASK 24 ***
In a special ranking system, each voter gives a rank from highest to lowest to all
teams participating in the competition.
The ordering of teams is decided by who received the most position-one votes. If two
or more teams tie in the first position, we consider the second position to resolve the
conflict, if they tie again, we continue this process until the ties are resolved. If two or
more teams are still tied after considering all positions, we rank them alphabetically
based on their team letter.

You are given an array of strings votes which is the votes of all voters in the ranking
systems. Sort all teams according to the ranking system described above.
Return a string of all teams sorted by the ranking system.
Example 1:
Input: votes = ["ABC", "ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation:
Team A was ranked first place by 5 voters. No other team was voted as first place, so team
A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.

Example 2:
Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position,
but X has one vote in the second position, while W does not have any votes in the second
position.
Example 3:
Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
Constraints:
1) 1 &lt;= votes.length &lt;= 1000
2) 1 &lt;= votes[i].length &lt;= 26
3) votes[i].length == votes[j].length for 0 &lt;= i, j &lt; votes.length.
4) votes[i][j] is an English uppercase letter.
5) All characters of votes[i] are unique.
6) All the characters that occur in votes[0] also occur in votes[j] where 1 &lt;= j &lt; votes.length.
"""

def task_24(votes):
    d = {}
    rangs = {}
    for i in range(0,len(votes[0])):
        rangs[i] = 21**(len(votes[0])-i)
    for vote in votes:
        for i, char in enumerate(vote):
            if char not in d:
                d[char] = 0
            d[char] += rangs[i]
        
    voted_names = sorted(d.keys())
    sorted_d = sorted(voted_names, key=lambda x: d[x], reverse=True)
        
    return "".join(sorted_d)


