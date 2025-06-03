
n = int(input())
taro = 0
hanako = 0

for i in range(n):
    columns = input().rstrip().split()
    tcard = columns[0]
    hcard = columns[1]
    if tcard > hcard:
        taro += 3
    elif hcard > tcard:
        hanako += 3
    else: 
        taro += 1
        hanako += 1
    
print(taro,hanako)
