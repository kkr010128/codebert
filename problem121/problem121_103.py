N = int(input())
A = "abcdefghijklmnopqrstuvwxyz"
x = [A[(N-1)%26]]
N -= 26
i = 1
while N > 0:
    x.append(A[((N-1)//(26**i))%26])
    i += 1
    N -= 26**i
ans = ""
for i in range(1,len(x)+1):
    ans += x[-i]
print(ans)