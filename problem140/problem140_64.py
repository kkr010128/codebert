# B
T = str(input())
try:
    for i in range(T.count("?")):
        index = T.index("?")
        if T[index - 1] == "P":
            T = T.replace("?","D",1)
        elif T[index + 1] == "D":
            T = T.replace("?","P",1)
        elif T[index + 1] == "?":
            T = T.replace("?","P",1)
        else:
            T = T.replace("?","D",1)
    print(T)
except:
    print(T.replace("?","D"))