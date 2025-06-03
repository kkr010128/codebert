N = int(input())
for i in range(10):
    ans = (i+1)*1000-N
    if ans >= 0:
        print(ans)
        exit()