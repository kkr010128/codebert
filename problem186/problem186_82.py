score = list(map(int,input().split()))
kenl = list(map(int,input().split()))

syoki = 0
syoki = kenl[0]+(score[0]-kenl[score[1]-1])
length = [0]*score[1]
length[0] = syoki
for i in range(score[1]-1):
    length[i+1] = kenl[i+1]-kenl[i]

length.sort()
answer = length[score[1]-1]
print(score[0]-answer)