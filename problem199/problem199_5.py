s = input().split("hi")

f = 0

for i in s:
    if i != "":
        f = 1
        break
    
if f == 0:
    print("Yes")
else:
    print("No")