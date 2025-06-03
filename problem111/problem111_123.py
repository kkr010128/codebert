N = int(input())
arr = sorted(list(map(int, input().split())),reverse=True)
arr2 = [arr[0]]

for i in range(1,N,1):
    arr2.append(arr[i])
    arr2.append(arr[i])


ans = 0
for i in range(N-1):
    ans += arr2[i]

print(ans)

