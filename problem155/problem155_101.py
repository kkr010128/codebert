word = list(map(int,input().split()))
hyoko = list(map(int,input().split()))
road = [0]*word[1]
for i in range(word[1]):
    road[i] = list(map(int,input().split()))
tenbo = [1]*word[0]

for j in range(word[1]):
    if hyoko[road[j][0]-1] > hyoko[road[j][1]-1]:
        tenbo[road[j][0]-1] *= 1
        tenbo[road[j][1]-1] = 0
    elif hyoko[road[j][0]-1] < hyoko[road[j][1]-1]:
        tenbo[road[j][0]-1] = 0
        tenbo[road[j][1]-1] *= 1
    else:
        tenbo[road[j][0]-1] = 0
        tenbo[road[j][1]-1] = 0
answer = word[0] - tenbo.count(0)
print(answer)