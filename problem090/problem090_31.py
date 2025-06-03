S = list(str(input()))

count = 0
max = 0

for i in range(3):
    if S[i] == "R":
        count += 1
    else:
        if max < count:
            max = count
        count = 0
if max < count:
    max = count

print(max)