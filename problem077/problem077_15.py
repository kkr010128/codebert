arr = input().split()

a = int(arr[0])
b = int(arr[1])

c = int(arr[2])
d = int(arr[3])

tmp = []
tmp.append(a*c)
tmp.append(a*d)
tmp.append(b*c)
tmp.append(b*d)

ans = max(tmp)

print(ans)