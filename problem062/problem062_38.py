num = int(input())
while num != 0:
    sum = 0
    k = 1
    while num>=k:
        sum = sum + num%(k*10)//k
        k = k*10
    print(sum)
    num = int(input())