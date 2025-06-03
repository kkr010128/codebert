
from collections import Counter
a = int(input())
num_list = list(map(int, input().split()))
D = Counter(num_list)
for i in range(a):
    print(D[i+1])