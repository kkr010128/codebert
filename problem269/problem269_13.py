T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split()) #高橋君
B1,B2 = map(int,input().split()) #青木君

D1,D2 = (A1-B1)*T1, (A1-B1)*T1+(A2-B2)*T2

if D1*D2 > 0:
    print(0)
elif D2 == 0:
    print("infinity")
else:
    if -D1%D2 == 0:
        print(-D1//D2*2)
    else:
        print(-D1//D2*2+1)