N = int(input())
S = list(input())
r = 0
g = 0
b = 0

for i in range(N):
    if S[i] == 'R':
        r += 1
    elif S[i] == 'G':
        g += 1
    else:
        b += 1

allcnt = r * g * b

sub = 0
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            None
        else:
            k = 2*j-i
            if k >= N or S[i] == S[k] or S[j] == S[k]:
                None
            else:
                sub += 1

print(allcnt - sub)