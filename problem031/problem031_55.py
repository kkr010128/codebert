for i in range(1000):
    n = int(input())
    if n == 0:
        exit()
    s = list(map(int,input().split()))
    ave = sum(s) / len(s)
    num = 0
    for j in s:
        num += (j-ave)**2
    num /= len(s)
    print(num**(1/2))
