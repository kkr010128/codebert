from collections import Counter
D = int(input())
c = list(map(int, input().split()))
s = []
for i in range(D):
    temp_s = list(map(int, input().split()))
    s.append(temp_s)
my_count = Counter()
t = list(int(input()) for i in range(D))
c_sum = sum(c)
my_sum = 0
my_minus = 0
for d in range(D):
    my_count [t[d]] = c[t[d] - 1] * (d + 1)
    my_sum += s[d][t[d] - 1]
    my_minus += sum(dict(my_count).values()) - c_sum * (d + 1)
    print(my_sum + my_minus)