while True:
    mid,final,re = map(int,input().split())
    if mid==final==re==-1: break
    elif mid==-1 or final==-1:
        print("F")
    elif mid+final>=80:
        print("A")
    elif 65<= mid+final <80:
        print("B")
    elif 50<= mid+final <65:
        print("C")
    elif 30<= mid+final <50:
        if re>=50:
            print("C")
        else:
             print("D")
    elif mid+final <30:
        print("F")