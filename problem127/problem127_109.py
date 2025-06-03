x, y = map(int, input().split())

flag = 0

for i in range(101):
    for j in range(101):
        if i+j == x:
            if 2*i+4*j == y:
                print("Yes")
                flag += 1
                break
    else:
        continue
    break

if flag==0:
    print("No")



