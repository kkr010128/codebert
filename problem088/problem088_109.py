n = int(input())
a = list(map(int, input().split()))

tmp = 0
sum = 0
for i in a:
    if tmp > i:
        dif = tmp - i
        sum += dif
    else:
        tmp = i

print(sum)
    
