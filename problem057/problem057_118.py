while True:
    m,f,r = map(int,input().split())
    score = ""
    if(m == -1 and f == -1 and r == -1): break
    if(m == -1 or f == -1): score = "F"
    elif(m+f >= 80): score = "A"
    elif(m+f >= 65): score = "B"
    elif(m+f >= 50): score = "C"
    elif(m+f >= 30):
        if(r >= 50): score = "C"
        else: score = "D"
    else:
        score = "F"
    print(score)
    
