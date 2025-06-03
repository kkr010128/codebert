T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
# 必ずB1の方を大きくする必要がある
if A1 > B1:
    B1, A1 = A1, B1
    B2, A2 = A2, B2
P = T1*(A1-B1)  # Pは負の値
Q = T2*(A2-B2)
if P + Q == 0:
    print("infinity")
    exit()
elif P + Q < 0:  # 出会う位置まで戻ってこれなかった
    print(0)
    exit()
elif P + Q > 0:  # 限られた数だけあえる
    if (-P % (P + Q)) == 0:
        print(2*(-P // (P+Q)))
    else:
        print(2*(-P // (P+Q))+1)
