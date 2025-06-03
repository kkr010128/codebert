if __name__ == "__main__":
    while True:
        a,op,b = map(str,input().split())
        if op is "+":
            print("%d"%(int(a)+int(b)))
        elif op is "-":
            print("%d"%(int(a)-int(b)))
        elif op is "*":
            print("%d"%(int(a)*int(b)))
        elif op is "/":
            print("%d"%(int(a)/int(b)))
        else:
            break