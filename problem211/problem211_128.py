i = list(map(int, input().split()))
N = i[0]
R = i[1]

if N <= 10:
    print(R + (100*(10 - N)))
else:
    print(R)