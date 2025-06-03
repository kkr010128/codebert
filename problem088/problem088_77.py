num = input()
list = input().split()

ans = 0

for i in range(int(num) - 1):
    n1 = int(list[i])
    n2 = int(list[i+1])

    if  n1 > n2 :
        ans += (n1 - n2)
        list[i+1] = list[i]
    else:
        ans += 0

print(ans)