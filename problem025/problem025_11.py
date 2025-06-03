n = int(input())
arr = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

result = set()
for i in range(2**n):
    tmp = 0
    for j in range(n):
        if i >> j & 1:
            tmp += arr[j]
    result.add(tmp)

for x in m:
    print("yes" if x in result else "no")
