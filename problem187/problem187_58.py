#６回目、2020-0612
#2重ループ　＋O(1)
#i,jがループの中か外で場合分け

#初期入力
N, x, y = map(int, input().split())

ans ={i:0 for i in range(1,N)}
for i in range(1,N):
    for j in range(i+1,N+1):
         #（i,jがループより共に左、ともに右）
        if (j <=x or y <=i) :
            ans[j-i] +=1
        # （iがループより左 and jがループより右）
        elif i <=x and y <=j:
            ans[x-i +1 +j-y] +=1
        # i,jが共にループの中
        elif x <i and j <y:
            dist =min(j-i,i-x + y-j +1) #時計回りと反時計回りの短いほう、+1はxとyを結んだ部分
            ans[dist] +=1
        # iがループより左、jがループの中
        elif i <=x and j < y:
            dist =x-i + min(j-x , y+1-j)
            ans[dist] +=1 
        # iがループの中、jがループの右
        elif x <i and y <=j:
            dist =min(y-i , 1 +i-x) + j-y
            ans[dist] +=1 

#答え出力
for i in range(1,N):        
    print(ans[i])