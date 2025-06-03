from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a += list(range(1,n+1))
a = Counter(a).most_common()
a.sort()
for i,j in a:
    print(j-1)