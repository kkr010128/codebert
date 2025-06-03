K=int(input())
s =input()
x = len(s)

if x<=K:
    print(s)
else:
    print(s[:K]+'...')