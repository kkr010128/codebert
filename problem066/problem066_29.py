while True:
    x=input()
    if x == "-":
        break
    y=int(input())
    for i in range(y):
        z=int(input())
        x=x[z:]+x[:z]
    print(x)
