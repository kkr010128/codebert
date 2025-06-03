#In[]:
x = int(input())

money = 100
year = 0

while True:
    money += money//100
    year += 1

    if money >= x:
        print(year)
        break