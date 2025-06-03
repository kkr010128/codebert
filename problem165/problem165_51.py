import collections
N = int(input())
A = []
for i in range(N):
    A.append(input())
dic = collections.Counter(A)
print(len(dic.keys()))