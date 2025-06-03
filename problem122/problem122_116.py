n = int(input())
A = list(map(int, input().split()))
freq = [0]*(10**5+1)

for a in A:
    freq[a] += 1
q = int(input())
ans = sum(A)
for i in range(q):
    b, c = map(int, input().split())
    ans -= freq[b] * b
    freq[c] += freq[b]
    ans += freq[b] * c
    freq[b] = 0
    print (ans)