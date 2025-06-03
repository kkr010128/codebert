N, M = map(int, input().split())
l = [[] for _ in range(N)]
for i in range(M):
    p, s = input().split()
    l[int(p) - 1].append(s)

correct = 0
penalty = 0
for ll in l:
    if 'AC' not in ll:
        continue
    correct += 1
    penalty += ll.index('AC')

print(correct, penalty)