n = int(input())
aas = list(map(int, input().split()))
arr = [0]*(10**5+1)
res = 0
for i in aas:
    arr[i] += 1
    res += i
q = int(input())
for i in range(q):
    b,c = map(int, input().split())
    res += (c-b)*arr[b]
    print(res)
    arr[c] += arr[b]
    arr[b] = 0