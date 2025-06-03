import math
N = int(input())

N_d = []
N1_d = []
answer = set()
for i in range(1,math.ceil(N**0.5)+1):
    if N%i == 0:
        N_d.append(i)
        N_d.append(N//i)

for i in range(len(N_d)):
    temp = N
    while temp % N_d[i] == 0:
        temp = temp//N_d[i]
        if N_d[i] == 1:
            break
        
    if temp % N_d[i] == 1:
        answer.add(N_d[i])


for i in range(1,math.ceil((N-1)**0.5)+1):
    if (N-1) %i == 0:
        answer.add(i)
        answer.add((N-1)//i)

answer.remove(1)
print(len(answer))