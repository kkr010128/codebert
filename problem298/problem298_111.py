n, k = map(int, input().split())
h = list(map(int, input().split()))
ok_list = list()
for data in h:
    if data >= k:
        ok_list.append(data)
print(len(ok_list))