n, m = map(int, input().split())
ar = list(map(int, input().split()))

add = sum(ar)
check = add / (4 * m)
amt = 0

for num in ar:
    if num >= check:
        amt += 1

if amt >= m:
    print("Yes")
else:
    print("No")









            

