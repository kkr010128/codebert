N = int(input())
t = 0
h = 0
for n in range(N):
    w = input().split()
    if w[0] == w[1]:
        t += 1
        h += 1
    elif w[0] > w[1]:
        t += 3
    else:
        h += 3
print(t,h)
