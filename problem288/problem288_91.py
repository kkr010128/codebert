N = int(input())
for i in range(1,int(N**(1/2)) + 1)[::-1]:
    if N%i == 0:
        print(i + N//i - 2)
        exit()