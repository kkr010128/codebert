N,M=map(int, input().split())
a = list(map(int, input().split()))
z = sum(a)
a.sort(reverse=True)

for i in a[:M]:
    if i < z/4/M:
        print('No')
        break
else:
    print('Yes')