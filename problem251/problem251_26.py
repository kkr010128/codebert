n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()

hand=["" for _ in range(k)]
point=[0 for _ in range(k)]

for i in range(n):
    index=i%k
    #初めの手（制限なし）
    if index==i:
        if t[i]=="r":
            hand[index]="p"
            point[index]+=p
        elif t[i]=="s":
            hand[index]="r"
            point[index]+=r
        else:
            hand[index]="s"
            point[index]+=s
    #２番目以降の手
    else:
        if t[i]=="r":
            if hand[index]=="p":
                hand[index]="x"
            else:
                hand[index]="p"
                point[index]+=p
        elif t[i]=="s":
            if hand[index]=="r":
                hand[index]="x"
            else:
                hand[index]="r"
                point[index]+=r
        else:
            if hand[index]=="s":
                hand[index]="x"
            else:
                hand[index]="s"
                point[index]+=s

print(sum(point))