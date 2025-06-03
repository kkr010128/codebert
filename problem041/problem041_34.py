w,h,x,y,r=map(int, input().split())

x_max=int(x+r)
x_min=int(x-r)
y_max=int(y+r)
y_min=int(y-r)

#print(x_max,x_min,y_max,y_min)


if y_max > h:
    print("No")
else:
    if y_min < 0:
        print("No")
    else:
        if x_max > w:
            print("No")
        else:
            if x_min < 0:
                print("No")
            else:
                print("Yes")