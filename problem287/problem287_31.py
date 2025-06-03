n = int(input())
flag = False
for x in (range(1,10)):
    for y in (range(1,10)):
        if x * y == n:
            flag = True
    else:
        continue
    break
    

if flag:
    print("Yes")
else:
    print("No")
