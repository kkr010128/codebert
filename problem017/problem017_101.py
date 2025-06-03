n = int(input())
A = list()
for i in range(0, n):
    A.append(int(input()))

G = [1]  # G[0]????????¨?????????
cnt = 0

# G[i] = 3*Gi-1 + 1
for i in range(1, 100):
    h = 4**i + 3*2**(i-1) + 1
    if(h > n):  # h???n?¶???????????????§?????????4n+3*2n-1+1
        m = i
        break
    else:
        G.append(h)


for g in reversed(G):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v


print(m)
print(" ".join(str(x) for x in reversed(G)))
print(cnt)

print("\n".join(str(x) for x in A))