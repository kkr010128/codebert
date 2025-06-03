def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,k = MI()
R,S,P = MI()
T = input()
li = [[] for _ in range(k)]
for i in range(len(T)):
    j = i%k
    li[j].append(T[i])
score = 0
for i in range(k):
    prev = "-1"
    for j in range(len(li[i])):
        if li[i][j] == "r":
            if prev == "p":
                prev = "-1"
            else:
                score += P
                prev = "p"
        if li[i][j] == "s":
            if prev == "r":
                prev = "-1"
            else:
                score += R
                prev = "r"
        if li[i][j] == "p":
            if prev == "s":
                prev = "-1"
            else:
                score += S
                prev = "s"
print(score)