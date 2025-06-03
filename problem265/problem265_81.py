n=int(input())
if (((n/1.08)//1)*1.08)//1==n:
    print(int((n/1.08)//1))
elif (((n/1.08)//1+1)*1.08)//1==n:
    print(int(((n+1)/1.08)//1))
else:
    print(":(")