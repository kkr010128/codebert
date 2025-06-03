weather = list(input())

i = 0
j = 0
days = 0
consecutive = []

while i <= 2:
    while i + j <= 2:
        if weather[i+j] == "R":
            days += 1
            j += 1
        else:
            break
    i += 1
    j = 0
    consecutive.append(days)
    days = 0

print(max(consecutive))
