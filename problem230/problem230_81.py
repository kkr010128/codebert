n, d, a = map(int, input().split())
XH = []
for i in range(n):
    x, h = map(int, input().split())
    XH.append((x, h))
XH.sort()
X = [x for x, h in XH]
H = [h for x, h in XH]
# n, d, a = 9, 2, 2
# X = [1, 3, 4, 6, 9, 10, 12, 13, 16]
# H = [7, 6, 7, 5, 10, 3, 8, 9, 6]
X.append(10**10)
H.append(0)
j = 0
c = 0
S = [0]*(n+1)
for i in range(n):
    H[i] = max(0, H[i]-S[i])
    c += -(-H[i]//a)
    while X[j] <= X[i] + 2*d:
        j += 1
    S[i+1] += S[i] + -(-H[i]//a)*a
    S[j] -= -(-H[i]//a)*a
    # print(i)
    # print(H)
    # print(S)
# print(H)
# print(S)
print(c)
