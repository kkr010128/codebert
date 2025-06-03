        
try:
    inp = input().split()
    L = int(inp[0])
    R = int(inp[1])
    d = int(inp[2])
    
    if L >= 1 and R >= 1 and L <= R and L<=100 and R<=100 and d>=1 and d<=100:
        counter = 0
        for i in range(L,R+1):
            if i%d == 0:
                counter += 1
        print(counter)
        
except Exception as e:
    print(e)