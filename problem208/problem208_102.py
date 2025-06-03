n,m=map(int,input().split())

ans=["#"]*n
for _ in range(m):
    s,c=map(int,input().split())
    # 同じ桁に複数の指示が飛んできたら狩猟
    if not ans[s-1] in["#",c]:
        print(-1)
        exit()
    ans[s-1]=c

#　nが一桁の時の対応
if len(ans)==1:
    print(0 if ans[0]=="#" else ans[0])
    exit()
#頭の数字について
if ans[0]==0:
    print(-1)
    exit()

if ans[0]=="#":
    ans[0]=1

for num in ans:
    print(num if num!="#" else 0,end="")
