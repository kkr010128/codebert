N = int(input())
Alist = list(map(int,input().split()))
Answer = 1
if 0 in Alist:
    Answer = 0
for i in range(N):
    Answer *= Alist[i]
    if Answer > 10**18:
        Answer = -1
        break
print(Answer)