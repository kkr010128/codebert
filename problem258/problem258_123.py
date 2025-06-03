N = int(input())
if N % 2 ==1:
    print(0)
    exit()
else:
    count =0
    N = N//2
    while N //5:
        N = N//5
        count +=N


print(count)