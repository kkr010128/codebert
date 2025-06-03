from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a = Counter(a).most_common()
if len(a) == n:
    print('YES')
else:
    print('NO')