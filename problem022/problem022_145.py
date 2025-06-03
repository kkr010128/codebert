n = int(input())
S = list(map(int, input().split(' ')))
q = int(input())
T = list(map(int, input().split(' ')))
counter = 0
for t in  T:
    for s in S:
        if(s == t):
            counter += 1
            break

print(counter)

