A = int(input())
B = int(input())

ans = {1, 2, 3}
ans -= {A, B}
print(ans.pop())
