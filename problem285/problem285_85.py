S = input()
N = len(S)+1
x = [0 for _ in range(N)]
l = 0
while(l<N-1):
    r = l+1
    while(r<N-1 and S[r]==S[l]):
        r += 1
    if S[l]=='<':
        x[l] = 0
        for i in range(l+1, r+1):
            x[i] = max(x[i], x[i-1]+1)
    else:
        x[r] = 0
        for i in range(r-1, l-1, -1):
            x[i] = max(x[i], x[i+1]+1)
    l = r
print(sum(x))