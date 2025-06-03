a,b,c=map(int, input().split())
#たこ焼きが余るかの場合分け
if a%b==0:
    Q=a//b
    #ちょうど焼ききる
else:
    Q=a//b+1
    #余る
print(Q*c)#回数×時間
#完了
