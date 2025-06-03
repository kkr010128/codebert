n = int(input())
r = [int(input()) for i in range(n)]
start = r[0]
score = r[1] - r[0]
for i in range(1,n):
    if r[i] - start > score: score = r[i] - start
    if r[i] < start: start = r[i]
print(score)