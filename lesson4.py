import random
import sys
import itertools
from functools import reduce
from math import factorial



# #1 =============================================================
#/usr/bin/python3
# a, b, c = argv
# res = (a * b) + c
# print("total:" res)
#2 =============================================================

# li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_li = [j for i, j in zip(li, li[1:]) if j > i]
# print(new_li)

#3 ==================================================================
# li = [i for i in range(20, 241)  if i % 20 == 0 or i % 21 == 0]
# print(li)

#4 ==================================================================
# li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# for i in li:
#    if li.count(i) == 1:
#        print(i)

#5===============================================================
# li = [i for i in range(100,1000) if i % 2 == 0]
# sum = reduce((lambda x, y: x * y), li)
# print(summa)

#6 ===============================================================

# for el in count(7):
# print(el)
#
# с = 0
# for el in cycle("ABC"):
# if с > 10:
# break
# print(el)
# с += 1

#7 =================================================================
#
# def fibo_gen():
#     for el in count(1):
#         yield factorial(el)
