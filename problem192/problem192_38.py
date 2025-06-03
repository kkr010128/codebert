import numpy as np

N=int(input())
A=np.array(list(map(int,input().split())))
'''
以下、方針
・Aから、各要素の出現回数を取得する。
・出現回数から、組み合わせを計算する。
'''
uni,cou=np.unique(A,return_counts=True)

# print(uni)
# print(cou)
dic0={}
dic1={}
dic={} #回答用

com=[]
for i in range(len(cou)):
    c=cou[i]*(cou[i]-1)//2
    dic0[uni[i]]=cou[i]
    dic1[uni[i]]=c
    com.append(c)
    dic.setdefault(uni[i])

# print(com)
totalcombination=sum(com)

# print(com)
# print(dic1)

'''
以下方針
・Aから数字を取得
・その数字に対応する組み合わせを減らす。
・その数字の出現回数を1減らした状態の組み合わせの数を足す。
'''

for j in range (N):
    n=A[j] #nはAの数列の数字
    if dic[n]==None:
        e=(dic0[n]-1)*(dic0[n]-2)//2
        t=totalcombination-dic1[n]+e
        dic[n]=t
        print(t)
    else:
        print(dic[n])