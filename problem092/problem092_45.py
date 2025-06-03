x,k,d=map(int,input().split());xx=abs(x)
tmp=xx;tmp=(xx//d);cc=min(tmp,k)
xx-=d*cc;k-=cc;k&=1;xx-=d*k
print(abs(xx))