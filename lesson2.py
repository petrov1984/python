# # 1 =================================================
# li = [123, 'text', True, [0, 1]]
# for i in li:
#     print(type(i))

# # 2 ===================================================
# li2 = list(input("Type of your stupid values:"))
# li2[::2], li2[1::2] = li2[1::2], li2[::2]

# # 3 ===================================================
# dic = {'winter': [1, 2, 3], 'spring': [4, 5, 6], 'summer': [7, 8, 9], 'autumn': [10, 11, 12]}
# num = int(input("Enter a number:"))
# for i in dic:
#    if num in dic[i]:
#        print(i)

# 4 =====================================================
# string = list(input("Enter your stupid string:").split())
# for i, el in enumerate(string):
#     if len(el) > 10:
#         el = el[:10]
#     print(f"{i} {el}")

#5 ===========================================================
li3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = int(input("Enter number:"))
if ans in li3:
       a = li3.index(ans) + 1
       print(a)
       li3.insert(a, ans)
       print(li3)
elif ans not in li3:
       li3.insert(0, ans)
       print(li3)
else:
    print("Somthing went wrong")
