while True:
    a, op, b = map(str, raw_input().split())

    if op in "+":
        print int(a)+int(b) 
    elif op in "-":
        print int(a)-int(b)
    elif op in "*":
        print int(a)*int(b)
    elif op in "/":
        print int(a)/int(b)
    else :
        break;