#６回目、2020-0612
#2重ループ　＋O(1)
#場合分けを近道と通常のみ（絶対値を使う）

#初期入力
N, x, y = map(int, input().split())
normal =0
short =0
ans ={i:0 for i in range(1,N)}
for i in range(1,N):
    for j in range(i+1,N+1):
         normal =j -i
         short  =abs(x-i) +1 +abs(j-y)
         dist =min(normal,short)
         ans[dist] +=1
      

#答え出力
for i in range(1,N):        
    print(ans[i])