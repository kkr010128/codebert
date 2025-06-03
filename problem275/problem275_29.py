


def resolve():
    x,y=(int(i) for i in input().split())
    if x==1 and y==1:
        print(1000000)
        return
    c=0
    if x==1:
        c+=300000
    if x==2:
        c+=200000
    if x==3:
        c+=100000

    if y==1:
        c+=300000
    if y==2:
        c+=200000
    if y==3:
        c+=100000
    print(c)




if __name__ == "__main__":
    resolve()