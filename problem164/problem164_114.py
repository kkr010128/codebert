#https://atcoder.jp/contests/abc164/tasks/abc164_b
A,B,C,D = map(int,input().split())
Senkou_N,Senkou_Amari = divmod(C,B)
if Senkou_Amari != 0:
    Senkou_N += 1
Koukou_N,Koukou_Amari = divmod(A,D)
if Koukou_Amari != 0:
    Koukou_N += 1

if Senkou_N <= Koukou_N:
    print("Yes")
else:
    print("No")