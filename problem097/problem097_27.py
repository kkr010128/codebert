k = int(input())
l = []
if 7 % k == 0:
    print(1)
    exit(0)
l.append(7 % k)
for i in range(1,k):
    a = (10 * l[i-1] + 7)
    if a % k == 0:
        print(i+1)
        exit(0)
    else:
        l.append(a % k)
print(-1)    