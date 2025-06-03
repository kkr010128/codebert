
def havec(x_list, y):
    x_list[y-1] = 1
    
def printc(x_list, s):
    for i in range(13):
        if x_list[i] == 0:
            print("%s %d" %(s, i+1))

n = input()
Sp = [0,0,0,0,0,0,0,0,0,0,0,0,0]
Ha = [0,0,0,0,0,0,0,0,0,0,0,0,0]
Cl = [0,0,0,0,0,0,0,0,0,0,0,0,0]
Di = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    incard = raw_input()
    a, b = incard.split(" ")
    b = int(b)
    
    if a == "S":
        havec(Sp, b)
    elif a == "H":
        havec(Ha, b)
    elif a == "C":
        havec(Cl, b)
    else:
        havec(Di, b)

printc(Sp, "S")
printc(Ha, "H")
printc(Cl, "C")
printc(Di, "D")