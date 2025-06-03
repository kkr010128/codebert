S, T = input().split()
A, B = map(int, input().split())
U = input()

ans = {S: A, T: B}
ans[U] -= 1

print(ans[S], ans[T])