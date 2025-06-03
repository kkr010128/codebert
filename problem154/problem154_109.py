n, k = map(int, input().split())
d = [0] * k
a = []

for i in range(k):
    d[i] = int(input())
    a_in = list(map(int, input().split()))
    a.extend(a_in)

num = len(set(a))
print(n-num)