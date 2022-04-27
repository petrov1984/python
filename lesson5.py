import numbers
import sys

#1 ============================================================================
# words = input("Enter your words:")
# f = open("file.txt", "w+")
# f.write(words)
# w = f.read()
# print(w)
# f.close

#2 ============================================================================
# lines = 0
# words = 0
# for i in open("source.list", "r"):
#     lines += 1
#     pos = 'out'
#     for letter in line:
#         if letter != ' ' and pos == 'out':
#             words += 1
#             pos = 'in'
#         elif letter == ' ':
#             pos = 'out'
# print("Lines:", lines)
# print("Words:", words)

#3 ===========================================================================

# f = open("zp", "r")
# for i in f:
#     name, zp = i.split()
#     zp = int(zp)
#     if zp > 20000:
#      print(name)

#4 =========================================================================
# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# f = open("12", "r")
# f2 = []
# for i in f:
#      i = i.split(' ', 1)
#      f2.append(rus[i[0]] + ' ' + i[1])
# print(f2)
# total = open("new-file.txt", "w")
# total.writelines(f2)
# total.close

#5 ========================================================================
# f = open('file_5.txt', 'w+')
# line = input('Введите цифры через пробел \n')
# f.writelines(line)
# my_numb = line.split()
# print(sum(map(int, my_numb)))
