cnt = int(input())
chain = 0
first = 0
second = 0

for i in range(cnt):
    nList = list(map(int, input().split()))
    first = nList.pop()
    second = nList.pop()
    if first == second:
        chain = chain + 1
        if chain >= 3:
            break
    else:
        chain = 0

if chain >= 3:
    print("Yes")
else:
    print("No")
