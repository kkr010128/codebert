n = int(input())
s = input().split()
q = int(input())
t = input().split()
res = 0
for i in t:
    if i in s:
        res +=1
print(res)
