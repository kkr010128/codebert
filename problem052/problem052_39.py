n = int(input())

result = [""]
for i in range(3, n + 1):
    if i % 3 == 0:
        result.append(i)
    elif "3" in list((str(i))):
        result.append(i)
print(*result)