a, b = map(int, input().split())
flag = 0
for i in range(2000):
    if (i*0.08)//1 == a:
        if (i*0.1)//1 == b:
            print(i)
            flag += 1
            break

else:
    if flag == 0:
        print("-1")