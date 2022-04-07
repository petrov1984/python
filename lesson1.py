#the First task ========================================================
var1 = 1
var2 = 2
msg1 = int(input("Enter a number...."))
msg2 = input("Enter a word")
print(var1, var2, msg1, msg2)

#the Second one ============================================================
sec = int(input("Enter a number of seconds..."))
hours = ((sec // 60) // 60)
minutes = (sec // 60)
print(f"{hours}:{minutes}:{sec}")

# the Third task ==================================================
n = int(input("Enter 'N' number...."))
n2 = int(f"{n}{n}")
n3 = int(f"{n2}{n}")
print(n + n2 + n3)

# the Forth ===================================================================
number = list(input("Enter an itenger number...."))
r = max(number)
print(f"the bigest digist is {r}")

# the Fifth =============================================================
profit = float(input("Enter your profit....."))
expense = float(input("Enter your expense...."))
total = profit - expense
if profit > expense:
    employes = int(input("Enter number of your employes"))
    print(f"You are on the roll. "
          f"Your profit is {profit} now. "
          f"Your profit {total / employes} per employes. Congrats")
else:
    print(f"You are a looser")

# the Sixth task ==============================================================
day1 = float(input("How many kilometrs did you go?....."))
day2 = day1 * 10 / 100 + day1
day3 = day2 * 10 / 100 + day2
day4 = day3 * 10 / 100 + day3
day5 = day4 * 10 / 100 + day4
day6 = day5 * 10 / 100 + day5
totl = int(day6)
print(f"On sixth day he has run at least {totl} km")
