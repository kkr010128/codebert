
h, w = map(int, input().split())

while h != 0:
    s1 = "#"
    s2 = "."
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                if j % 2 == 0:
                    print(s1, end="")
                else:
                    print(s2, end = "")
            print()
                    
        else:
            for j in range(w):
                if j % 2 == 0:
                    print(s2, end="")
                else:
                    print(s1, end = "")
            print()
        
    print()    
    h, w = map(int, input().split())

