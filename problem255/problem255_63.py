n = int(input())
S,T = input().split()
result = ''
for s,t in zip(S,T):
    result += s
    result += t
print(result)