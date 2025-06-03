while 1:
    data = input()
    if "?" in data:
        break
    print(eval(data.replace("/","//")))