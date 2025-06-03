n, k = (int(i) for i in input().split())
list_h = sorted([int(i) for i in input().split()])
if list_h[-1] < k:
    print("0")
    exit()
count = 0
for count in range(0, n):
    if list_h[count] >= k: break
print(len(list_h[count:]))