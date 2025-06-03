n = int(input())
a = list(map(int, input().split()))

# a = np.array(a)
# ans = []
# while a.min() != 9999999:
#     min_index = a.argmin()
#     ans.append(min_index+1)
#     a[min_index] = 9999999

# print(' '.join([str(_) for _ in ans]))

l = []
for i in range(n):
    l.append([i+1, a[i]])

sl = sorted(l, key=lambda x: x[1])
sl0 = [r[0] for r in sl]
print(' '.join([str(_) for _ in sl0]))
