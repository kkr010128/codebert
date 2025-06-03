N = int(input())
ga = []
for _ in range(N):
    ga.append(input())
ga = set(ga)
print(len(ga))