n = int(input())
d = {}
ans = []

for i in range(n):
    order = list(map(str, input().split()))
    if order[0] == 'insert':
        d[order[1]] = i
    else:
        if d.__contains__(order[1]):
            ans.append('yes')
        else:
            ans.append('no')

print(*ans, sep='\n')

