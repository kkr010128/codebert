X = int(input())
# Xの素因数分解をうまくつかう
# A^5 - B^5 =(A-B)(A^4+A^3B+A^2B^2+AB^3+B^4)
# どっちが正負かは決まらない
# AB(A^2+B^2)+(A^2+B^2)^2-A^2B^2
# AB((A-B)^2+2AB)+((A-B)^2+2AB)^2 - A^2B^2
# A-B = P
# AB = Q
# A^5-B^5 = P(Q(P^2+2Q)+(P^2+2Q)^2-Q^2) = P(P^4+5P^2Q+5Q^2) = P(5Q^2+5P^2Q+P^4)
# Qは整数解なので
# 5Q^2+5P^2Q+P^4が整数解を持つ楽な方法は(Q+P)^2の形の時、つまり2P = P^2+2, 
# X = PRとする
# R-P^4は5の倍数になる

#Aの上限を求める
# X<10^9
# A-B = 1がAを最大にできる

maxA = 126
maxX = pow(10, 9)

flag = 0
for A in range(-126, 126):
    for B in range(-127, A):
        result = pow(A, 5) - pow(B, 5)
        if result > maxX:
            next
        if result == X:
            print(A, B)
            flag = 1
            break
    if flag == 1:
        break