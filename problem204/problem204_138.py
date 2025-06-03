S = input()
A = ["", ""]
Q = int(input())
b = 0
for _ in range(Q):
    query = input()
    if query[0] == "1":
        b ^= 1
    else:
        F = int(query[2])
        A[b^F-1] += query[4]
ans = A[0][::-1] + S + A[1]
if b:
    ans = ans[::-1]
print(ans)
