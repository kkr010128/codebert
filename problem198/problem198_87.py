n=int(input())
def make(floor,kind,name): #floor=何階層目か,kind=何種類使ってるか
    if floor==n+1: 
        print(name)
        return
    num=min(floor,kind+1)
    for i in range(num):
        use=0 #新しい文字使ってるか
        if kind-1<i:
            use=1
        make(floor+1,kind+use,name+chr(i+97))
make(1,0,"")       