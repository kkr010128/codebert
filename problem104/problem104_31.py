L, R, d  = map(int, input().split())
lst = list()
for x in range(R+1):
    y = d * x
    if y>=L and y<=R:
        lst.append(y)
print(len(lst))