while True:

    string = str(input())
    box = ""
    
    
    if string == "-":
        break
    
    shuffle = int(input())

    h = [0]*shuffle

    for a in range(shuffle):
        h[a] = int(input())

    for b in range(shuffle):
        box = string[0:h[b]]
        string = string[h[b]:]
        string = string+box
        box = ""

    print(string)
