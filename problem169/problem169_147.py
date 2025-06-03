N = int(input())
lst = list(map(int, input().split()))
anslst = [0]*N
for i in lst:
    anslst[i-1] += 1

for i in anslst:
    print(i)