square = []
while True:
    data = [int(e) for e in input().split()]
    if data[0]==0 and data[1]==0:
        break
    square.append(data)
    
for i in range(len(square)):
    for j in range(square[i][0]):
        for k in range(square[i][1]):
            print("#", end="")
        print()
    print()
