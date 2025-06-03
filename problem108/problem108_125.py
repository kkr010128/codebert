n = input()
if int(n)%1000 == 0:
    print(0)
elif int(n) < 1000:
    print(1000-int(n))
else:
    print(1000-int(n[-3:]))