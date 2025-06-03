N, R = list(map(int, input().split(' ')))
i = R if N >= 10 else R+100*(10-N)
print(i)