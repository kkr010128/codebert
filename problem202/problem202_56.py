N, A, B = map(int, input().split())
# 先頭からN個のボール, 列の末尾にA個の青ボール追加, B個の赤ボール追加

count = N // (A + B)
total = A * count + min(N - (A + B) * count, A)
print(total)