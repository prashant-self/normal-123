# a = 40
# b = 30
# sum = a + b
# mul = a * b
# if mul <= 1000:
#     print(mul)
# else:
#     print(sum)

x = "w3resource.com"
# x_len = len(x)
#print(x_len)

# x_len = 0
# for i in x:
#     x_len += 1
# print(x_len)

"""def find_len(x):
    x_len = 0
    for i in x:
        x_len += 1
    return x_len
word = find_len('w3resource.com')
print(word)"""


"""def frequency_char(str1):
    dict = {}
    for i in str1 :
        keys = dict.keys()
        if i in keys :
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(frequency_char("google.com"))"""


"""def string1(a):
    if len(a) > 2:
        return a[0:2] + a[-2:]
    elif len(a) == 2:
        return a + a
    else:
        return ' '
print(string1(input("enter string : ")))
print(string1(input("enter string : ")))
print(string1(input("enter string : ")))"""

"""srt1 = 'restart'
char = srt1[1:]
rep_char = srt1[0] + char.replace('r', '$')
print(rep_char)"""

"""a = 'abc'
b = 'xyz'

c = b[0:2]+a[-1] + " " + a[0:2] + b[-1]
print(c)"""

# def ly_ing(str1):
#     if len(str1) >= 3 and str1[-3:] == 'ing':
#         return str1 + 'ly'
#     elif len(str1) >=3 and str1[-3:] != 'ing':
#         return str1 + 'ing'
#     else:
#         return str1
# str2 = ly_ing(input("enter string : "))
# print(str2)


"""def ly_ing(str1):
    length = len(str1)
    if length > 2 :
        if str1[-3:] == 'ing':
            return str1 + 'ly'
        else :
            return str1 + 'ing'
    else:
        return str1
print(ly_ing('abc'))
print(ly_ing('ab'))
print(ly_ing('string'))"""

"""words = ['the', 'lyrics', 'is', 'poor', 'prashant']
char_length = []
big_char_len = 0
for i in words:
    char_length.append(len(i))
for n in char_length:
    if big_char_len < n:
        big_char_len = n
for m in words:
    if len(m)==big_char_len:
        print("longest word", m)
        print("length of word", big_char_len)"""

# str1 = 'prashant'
# str1 = str1[0:4] + str1[5:]
# print(str1)

# str1 = str1[-1] + str1[1:-1] + str1[0]
# print(str1)


"""str1 = 'abcde'
lst_str = ""
for i in range(len(str1)):
    if i % 2 == 0:
        lst_str += str1[i]
print(lst_str)"""

"""str2 = 'the quick brown fox jumps over the lazy dog'
dict = {}
words = str2.split()
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)"""

"""lst = [1,3,4]
sum = 1
for i in lst:
    sum *= i
print(sum)"""

"""nums = [20, 12, 15, 25]
large = 0
for i in nums:
    if large < i:
        large = i
print(large)"""

"""nums = [20, 12, 15, 25]
small = [0]
for i in nums:
    if i < small:
        small = i
print(small)"""

"""lrg = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in lrg:
    if len(i) > 1 and i[0] == i[-1] :
        count += 1
print(count)"""

# def last(n) :
#     return n[-1]
# def sorted_list(tuples):
#     return sorted(tuples, key = last)
# print(sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# lst = [1, 2, 1, 1, 2, 3, 3, 4, 4]
# lst1 = list(set(lst))
# print(lst1)

"""def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "the quick brown fox jumps over the lazy dog"))"""


"""def common_list(list1, list2):
    result = False
    for y in list1:
        for x in list2:
            if y == x:
                result = True
    return result
print(common_list([1,2,3,4,5], [5,6,7,8,9]))
print(common_list([1,2,3,4,5], [6,7,8,9]))"""

"""def remove_even(nums):
    odd_nums = []
    for i in nums:
        if i % 2 != 0:
            odd_nums.append(i)
    return odd_nums
print(remove_even([1,2,3,4,5,6,7,8,9,10]))"""


"""def addition(a, b):
    sum = a + b
    return sum
add = addition(12, 12)
print('addition of numbers ',add)
print('addition of two numbers is : ', addition(12, 13))"""


"""def next_num(a):
    next_number = a+1
    return next_number
print(next_num(23))"""

"""def convert_min_sec(min, sec):
    seconds = min * sec
    return seconds
print(convert_min_sec(3, 60))"""

def series_resistance(lst):
    total_ohms = 0
    for i in lst:
        total_ohms += i
    return total_ohms
print(series_resistance([1,5,6,3]))







