n = int(input())
l =list(map(int,input().split()))
l.reverse()
for i in range(n):
    if i != n-1:
        print(f"{l[i]} ",end="")
    else:
        print(f"{l[i]}")
