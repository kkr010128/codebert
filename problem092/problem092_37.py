##C - Walking Takahash
##正負が反転しないなら単調増加、減少
##反転するなら、反転した瞬間で残りの回数が偶数なら、その値、奇数なら、一つ前にの値
X,K,D = map(int,input().split())
##X1の正負フラグがあれば簡潔に書けるかも
if X < 0:
    X = -X
R = K - X // D
if X-K*D >= 0:
    print(X-K*D)
else:
    if R % 2 == 0:
        print(X - D*(X//D))
    else:
        print(abs(X - D*(X//D)-D))