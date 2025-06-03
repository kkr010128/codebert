a = []
for i in range(0,2):
    l = list(map(int,input().split()))
    a.append(l)
d = a[1][::-1]
print(' '.join(map(str,d)))