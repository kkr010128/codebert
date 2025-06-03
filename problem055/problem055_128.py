count =[[[0]*10 for j in range(3)] for k in range(4)]
n = int(input())
for x in range(n):
    b,f,r,v = map(int,input().split())
    # 1 <= b <=4
    # 1 <= f <= 3
    # 1 <= r <= 10
    # 1 <= v <= 9
    count[b-1][f-1][r-1] += v
    
for i in range(4):
    if i != 0:
        print("#"*20)
    for j in range(3):
        for k in range(10):
            print(f' {count[i][j][k]}',end="")
        print()
