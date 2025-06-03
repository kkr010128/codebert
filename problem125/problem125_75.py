p = int(input())
index = 1
while True:
    if p* index % 360 == 0:
        print(index)
        break
    index += 1