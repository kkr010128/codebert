while True:
    n = int(input())
    if(n == 0):
        break
    i = n%10
    x = n//10
    while(x):
        i = i + (x%10)
        x //= 10
    print(i)
