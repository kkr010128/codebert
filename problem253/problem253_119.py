N,A,B=map(int,input().split())
if (B-A)%2==0:
    print((B-A)//2)
else:
    if A-1<=N-B:
        #Aが1に到達するまで+AとBの距離が2の倍数になるまで
        x=A-1+1
        #Aは負け続け、Bは勝ち続ける
        y=(B-A)//2
        print(x+y)
        
    else:
        #BがNに到達するまで+AとBの距離が2の倍数になるまで
        x=N-B+1
        #Aは勝ち続け、Bは負け続ける
        y=(B-A)//2
        print(x+y)