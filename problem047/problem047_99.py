while True:
    a=input()
    b=a.replace("/","//")
    if "?" in b:
        break
    else:
        print(eval(b))