N = int(input())
S, T = map(list, input().split(' '))
result = ''
for s, t in zip(S, T):
    result = result + s + t
print(result)