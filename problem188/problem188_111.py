import heapq

X, Y, A, B, C = map(int, input().split())
apples = []
for x in input().split():
    apples.append((int(x), 'r'))
for x in input().split():
    apples.append((int(x), 'g'))
for x in input().split():
    apples.append((int(x), 'n'))
apples.sort()
apples.reverse()

r_count = 0
g_count = 0
n_count = 0
yummy = 0
for _ in range(A+B+C):
    apple = apples[_]
    if apple[1] == 'g' and not g_count == Y:
        g_count += 1
        yummy += apple[0]
    elif apple[1] == 'r' and not r_count == X:
        r_count += 1
        yummy += apple[0]
    elif apple[1] == 'n':
        n_count += 1
        yummy += apple[0]
    if g_count + r_count + n_count == X+Y:
        break
print(yummy)
