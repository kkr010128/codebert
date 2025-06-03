n = int(input())
for i in range(0, n):
    a, b, c = sorted(map(int, input().strip("\n").split(" ")))
    # a,b,c = sorted(input().strip("\n").split(" "))
    #print(a, b, c)
    if c*c - (a*a + b*b) == 0:
        print("YES")
    else:
        print("NO")