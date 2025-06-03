def resolve():
    X = int(input())
    if X >= 2100:
        print("1")
    else:
        if X%100 > (X//100)*5:
            print("0")
        else:
            print("1")
resolve()