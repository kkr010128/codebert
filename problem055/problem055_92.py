arr = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(int(input())):
    b,f,r,v = map(int, input().split())
    arr[b-1][f-1][r-1] += v
for i in range(4):
    for j in range(3):
        for k in range(10):
            if k == 0:
                print ("", end=" ")
            if k == 9:
                print(arr[i][j][k])
            else:
                print(arr[i][j][k], end=" ")
    if i != 3:
        print("#"*20)