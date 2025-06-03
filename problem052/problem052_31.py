def has_three(a):
    while a != 0:
        if a % 10 == 3:
            return True
        else:
            a /= 10
    return False


result = list()
n = int(raw_input())
for i in range(1, n + 1):
    if i % 3 == 0:
        result.append(i)
    elif has_three(i):
        result.append(i)
print(" " + " ".join(str(i) for i in result))