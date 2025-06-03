n = int(input())
l = sorted(list(enumerate(map(int,input().split()),start = 1)), key = lambda x:x[1])
print(*(l[i][0] for i in range(n)))