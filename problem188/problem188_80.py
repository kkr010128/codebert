X, Y, a, b, c = map(int, input().split())
A = list(map(int, input().split()))  # 赤色
B = list(map(int, input().split()))  # 緑色
C = list(map(int, input().split()))  # 無色, 赤色にも緑色にもなれる
A.sort(reverse=True)
B.sort(reverse=True)
# C.sort(reverse=True)

top_x_of_A = A[:X]
top_Y_of_B = B[:Y]
top_x_of_A.extend(top_Y_of_B)
C.extend(top_x_of_A)
C.sort(reverse=True)
print(sum(C[:X+Y]))
