m = input("")
s = m.split(".")
sum = 0
if len(s) == 1 and int(m)>=0 and int(m)<10**200000:
    for i in m :
        sum = sum+int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")