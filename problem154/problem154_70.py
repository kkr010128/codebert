n, k = map(int, input().split())
ans = set()
for i in range(k):
    d = input()
    a = set(map(int, input().split()))
    ans = ans | a  # 和集合をとる

print(n - len(ans))