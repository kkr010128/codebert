g = int(input("")) # get
a = False
for i in range(1,10):
    if (g % i == 0 and (g // i >= 1) and (g // i <= 9)):
        a = True
print("Yes" if (a) else "No")