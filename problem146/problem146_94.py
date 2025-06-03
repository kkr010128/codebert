def ggcd(a,b):
    if(b==0):
        return a
    return ggcd(b,a%b)
import math
import fractions
import collections
import itertools
import pprint
N=int(input())
l1=[]
adivb=[]
bis0=0
bdiva=[]
ais0=0
both0=0
p=10**9+7
fish=[list(map(int,input().split())) for _ in range(N)]
fishcomp=[]
d={}
for i in range(N):
    #イメージ的にはa/bを格納していく感じ
    #ai/bi==-bj/ajならダメ
    a=fish[i][0]
    b=fish[i][1]
    g=ggcd(a,b)
    if g!=0:        #ggcdの定義よりa=b=0なら0になりそう(a=0,b!=0ならb,逆もしかり)、つまり(a,0)(0,b)は(1,0)(0,1)にmapされる
        a=a//g
        b=b//g
    #ここらへんで、a,bをそのgcdで割ることによる正規化が完了しているはず
    if b<0:     #b<0の時に強制的にbを正の値に変換しても影響はない(これを噛ませると後々嬉しい)
        a=-a
        b=-b
    if (a!=0)or(b!=0):          #a=b=0でない時は(a,b)(-b,a)といった組みをなすことで仲が悪くなる。よって、(a,b)の連想配列を組んでそのペアを探す下準備
        if d.get(a)==None:
            d[a]={}
            d[a][b]=1
        else:
            if d[a].get(b)==None:
                d[a][b]=1
            else:
                val=d[a].get(b)
                d[a][b]=val+1
        fishcomp.append([a, b])
    else:                       #a=b=0の時は、単体でいてもダメなので、別カウント
        both0=both0+1
#print(d)
#print(fishcomp)
fishcomp=list(map(list,set(map(tuple,fishcomp))))   #二次元配列のset(地味にreferenceがないやつ)
#print(fishcomp)
length=N-both0                                      #とりあえずどっちも0なやつは制約なしには使えないので引く
#print(both0)
sets=[]
#以下ではai/bi==-bj/ajの組みを探している。d[a][b]の個数とd[-b][a]及びd[b][-a]の個数のみ探せば良い、ただ一方のみフォーカスして取ればok
#(a,b)のkeyにて(-b,a)のkeyを取れるか探すことをf(a,b)=(-b,a)としてmapするとf(f(a,b))=(-a,-b)となり、b>0より-b<0のキーは必ず存在しない
#一方f(a,b)=(b,-a)としてもf(f(a,b))=(-a,-b)より、逆方向のキーは存在せず、取れるときは一方向にしか取れない
#(ここでb>0が生きる)
#
for i in fishcomp:
    a=i[0]
    b=i[1]
    val1=d[a][b]
    #print(a,b,val1)
    if d.get(-b)!=None:
        if d[-b].get(a)!=None:
            val2=d[-b][a]               #(a,b)とペアにして都合の悪いものの個数
            sets.append([val1,val2])    #[(a,b)の個数,(-b,a)の個数]のペア
            length=length-(val2+val1)   #((a,b)の個数+(-b,a)の個数)個は自由に扱えなくなりました
#print(sets,length)
pro=1
for i in sets:
    #都合が悪いペアについては、(a,b)同士のみまたは(-b,a)同士のみしか含めることができない
    #よって都合が悪くなるペアごとに、(a,b)の方のみにフォーカスして使う/使わないをbinaryに考えたpow(2,#(a,b))こ、
    #(-b,a)の方のみにフォーカスして使う/使わないをbinaryに考えたpow(2,#(-b,a))こ、そこからどちらとも考えている空集合を1つひいて
    #P(ai,bi)=pow(2,#(ai,bi))+pow(2,#(-bi,ai))-1こが、あるペアP(ai,bi)のイワシを使って仲良くできる組み合わせ数である。
    #この組み合わせ数はペアごとに独立に決まるため、Π(i for allpairs)P(ai,bi)が制約あるイワシ同士で捻出できる選び方である
    pro=(pro*(pow(2,i[0],p)+pow(2,i[1],p)-1))%p
#print(pro)
print((pow(2,length,p)*pro-1+both0)%p)          #制約のないイワシの個数はlengthこで、その自由な選び方はpow(2,length)通り
#(制約のないイワシの選び方)*(都合の悪くなりうるイワシの選び方)で良いが、
#考察から除外した(0 0)のイワシは単体でのみいられるため、1匹につき1count増やし、(0匹)*(0匹)となる1通りを除外し、
#よってpow(2,length)*Π(i for allpairs)P(ai,bi)+both0-1が解である