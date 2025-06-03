import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

c_p = 0
c_q = 0
count = 0
for i in itertools.permutations(sorted(p),len(p)):

    if p == list(i):
        c_p = count
    if q == list(i):
        c_q = count
    count += 1

print(abs(c_p - c_q))