i = list(map(int, input().split()))

r = [ i[0]*i[2], i[1]*i[2], i[0]*i[3], i[1]*i[3] ]

print(max(r))