h =[2, 4, 5, 7, 9]
b = [0, 1, 6, 8]
p = [3]
n = int(input())
x = int(n) - (int(int(n)/10)*10)
for i in h:
    if i == x:
        print("hon")
for i in b:
    if i == x:
        print("pon")
for i in p:
    if i == x:
        print("bon")