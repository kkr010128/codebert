from collections import deque

X, K, D = map(int, input().split())

# まずは何回目で符号が逆転するかを算出
num_reverse = abs(X) // D + 1
if num_reverse > K:
    print(abs(X) - (K * D))
else:
    K -= num_reverse
    ans = abs(X) - (num_reverse * D)
    if K % 2 == 0:
        print(abs(ans))
    else:
        print(abs(abs(ans) - D))


