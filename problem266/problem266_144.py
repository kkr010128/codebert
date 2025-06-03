x = int(input())
li = [0]*100105
li[0] = 1
for i in range(x):
    if li[i] == 1:
        for j in range(6):
            li[i+j+100] = 1
print(li[x])