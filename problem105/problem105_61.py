input()
li = list(map(int, input().split()))
result = 0
for i in range(len(li)):
    if (i + 1) % 2 == 1:
        if li[i] % 2 == 1:
            result += 1
print(result)

