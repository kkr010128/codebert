kuri_now = False
cost = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
kuri = [0, 0, 0, 0, 0, 0.5, 1, 1, 1, 1, 1]
result = 0
for digit in reversed(input()):
    digit = int(digit)
    if kuri_now == 0:
        result += cost[digit]
        kuri_now = kuri[digit]
    elif kuri_now == 1:
        result += cost[digit + 1]
        kuri_now = kuri[digit + 1]
    else:
        if cost[digit] <= cost[digit + 1]:
            result += cost[digit]
            kuri_now = kuri[digit]
        else:
            result += cost[digit + 1]
            kuri_now = kuri[digit + 1]
if kuri_now == 1:
    result += 1
print(result)