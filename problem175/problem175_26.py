N = int(input())
S = input()
r,g,b = S.count('R'),S.count('G'),S.count('B')
#rgbでr,g,bがすべて異なる組み合わせ数
total = r*g*b
# そこからj-i=k-jの組み合わせを引く
for i in range(0,N-2):
    for j in range(i+1,N-1):
        k = 2*j-i
        if k >= N: break;
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            total-=1
# flg = [[[0 for i in range(N)] for j in range(N)] for k in range(N)]

print(total)
