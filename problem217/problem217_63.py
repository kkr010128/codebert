n = int(input())
a = list(map(int, input().split()))
count = 0

for i in a:
    if i % 2 ==0:
        if i % 3 != 0 and i % 5 != 0:
            count+= 1


if count >= 1:
    print("DENIED")
else:
    print("APPROVED")
