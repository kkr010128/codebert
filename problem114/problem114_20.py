D=int(input())                                          #コンテの日数
c=list(map(int,input().split()))                        #26タイプ(AAC~AZC)のコンテストの満足度低下度
s=[list(map(int,input().split())) for _ in range(D)]    #s[d][i]...d(1<=d<=D)日目にi(1<=i<=26)番目のコンテストを行った時の満足度上昇
types=[int(input()) for _ in range(D)]                  #コンテタイプ(1~26)
#満足度低下はΣ(1<=i<=26)ci*(d-last(d,i))                  #なおlast(d,i)=d日目以前に最後にタイプiのコンテストをやった日にち(ない場合0)
#よって満足度はs[d][i]-Σ(1<=i<=26)ci*(d-last(d,i))
#i日目のスコアはmax(10^6+s[d][i]-Σ(1<=i<=26)ci*(d-last(d,i)),0)
last=[0]*26                                             #typeごとに、最後に使われた日にちを記録するよ
typ=0
ans=0
for i in range(D):
    typ=types[i]-1
    score=s[i][typ]
    dwn=0
    last[typ]=(i+1)
    for j in range(26):
        dwn=dwn+c[j]*((i+1)-last[j])
    ans=ans+(score-dwn)
    #print(score,last)
    print(ans)
    #input()
