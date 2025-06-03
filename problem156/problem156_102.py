def getval():
    return int(input())

def main(x):
    for i in range(-200,201):
        flag = False
        for j in range(-200,201):
            if i**5-j**5==x:
                print("{a} {b}".format(a=str(i),b=str(j)))
                flag = True
                break
        if flag:
            break
                
                

if __name__=="__main__":
    main(getval())