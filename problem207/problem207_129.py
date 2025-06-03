
def main():
    a = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    x = [[0]*3 for _ in range(3)]
    b =[]
    for _ in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                x[i][j] = 1
    
    for i in range(3):
        c = 1
        for j in range(3):
            c *= x[i][j]
        if c == 1:
            print("Yes")
            return
    for i in range(3):
        c = 1
        for j in range(3):
            c *= x[j][i]
        if c == 1:
            print("Yes")
            return
    c = 1
    for i in range(3):
        c *= x[i][i] 
    if(c):
        print("Yes")
        return
    if(x[0][2]*x[1][1]*x[2][0]):
        print("Yes")
        return
    print("No")
    

    
    

if __name__ == "__main__":
    main()