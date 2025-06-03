S = input()
K = int(input())

if len(set(S)) == 1:
    print(len(S)*K//2)
    exit()

b = [1]
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        b[-1] += 1
    else:
        b.append(1)

ans = 0
for i in b:
    ans += i//2
ans *= K

if S[0] == S[-1] and b[0]%2 == b[-1]%2 == 1:
    ans += K - 1
print(ans)