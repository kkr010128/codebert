N = int(input())
n = input().split()
a = []
for i in range(N):
    a.append(int(n[i]))
a = sorted(a)
print('{0} {1} {2}'.format(a[0], a[-1], sum(a)))