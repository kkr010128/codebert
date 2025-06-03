point = int(input())
rank = 1

for val in range(1800, 200, -200):
    if point >= val:
        break
    else:
        rank += 1
print(rank)   