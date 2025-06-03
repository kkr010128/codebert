a=list(map(int,input().split()))

string=str(a[0]//a[1])+" "+str(a[0]%a[1])+" "+str("%.10f"%(a[0]/a[1]))
print(string)