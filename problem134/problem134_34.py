n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr) #配列を昇順ソートしておく(配列に0がある場合0が先頭に来るので、場合分けの必要がなくなる)
ans=1
for val in arr:
 ans*=val #Pythonは多倍長整数をサポートしているので単に積を求めれば十分
 if ans>10**18:
   print(-1)
   break
else:
 print(ans)