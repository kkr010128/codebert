# 初期入力
NN,K = (int(x) for x in input().split())

#K個の和、初項と修項
p =10**9 + 7
seq =[i for i in range(NN+1)] #0-Nまでの数列
ans =[0] *(NN+1)
st =[0]*(NN+1)
fi =[0]*(NN+1)
st[0] =sum(seq[  :K])
fi[0] =sum(seq[-K: ])
ans[0] =fi[0] -st[0] +1
if NN==1 and K==1:
    print(3)
else:
    for i in range(NN -K+1):
        st[i+1] =st[i] +seq[K+i]
        fi[i+1] =fi[i] +seq[-K-i-1]
        ans[i+1] =(fi[i+1] -st[i+1] +1)
    print(sum(ans) %p)