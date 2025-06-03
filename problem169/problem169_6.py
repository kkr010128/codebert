n = int(input())
a = list(map(int, input().split()))

menber = [0]*n

for value in a:
    menber[value-1] += 1
    
for i in menber:
    print(i)