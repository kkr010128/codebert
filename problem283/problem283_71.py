N = int(input())

count = 0

if N % 2 == 0:
    for i in range(1,int(N/2)):
        if i != N-i:
            count+=1
else:
    for i in range(1,int(N/2)+1):
        if i != N:
            count+=1
print(count) 