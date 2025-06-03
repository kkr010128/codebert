from collections import Counter
n=int(input())
a=list(map(int,input().split()))
dic=Counter(a)
for val in dic.values():
    if val>=2:
        print("NO")
        exit()
print("YES")