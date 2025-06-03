while True:
    n = int(input())
    if n == 0: break
    nsum = 0
    while n != 0:
        nsum += n%10
        n = n//10
    print(nsum)