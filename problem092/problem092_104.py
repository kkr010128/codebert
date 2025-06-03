#座標はxは負の場合もあるの絶対値をとること
X, K, D = list(map(int, input().split()))
X = abs(X)
#K回繰り返すことを考慮すること
i = min(X//D, K) #移動回数が最小の方をとる
X = X - i*D
K = K - i

if K > 0:
    if K % 2 == 1:
        X = X - D
print(abs(X))