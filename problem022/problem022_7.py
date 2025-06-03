n = int(input())
str = input().split(" ")
S = [int(str[i]) for i in range(n)]
q = int(input())
str = input().split(" ")
T = [int(str[i]) for i in range(q)]

S_set = set(S)
S = list(S_set)
T.sort()

result = 0

for s in S:
    for t in T:
        if s == t:
            result += 1
            break
        

print(result)
        



