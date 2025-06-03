n = int(input())
tmp = n // 1.08
if tmp * 1.08 // 1 == n:
    print(int(tmp//1))
elif (tmp + 1) * 1.08 // 1 == n:
    print(int((tmp + 1)//1))
else:
    print(":(")