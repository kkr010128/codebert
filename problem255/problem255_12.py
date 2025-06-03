N = int(input())
S, T = input().split()

i = ''
for j in zip(S, T):
    for k in j:
        i += k
print(i)