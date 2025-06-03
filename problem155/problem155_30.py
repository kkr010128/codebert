n,m = map(int, input().split())

ans = 0

#辺を取り除くことはabのセットとなっている要素から取り除くことと等価。頂点を消すのではない。
h_list = list(map(int, input().split()))
c = 0
max_list = [0]*(n+1)

for i in range(m):
    a,b = map(int, input().split())

    max_list[a] = max(max_list[a],h_list[b-1])
    max_list[b] = max(max_list[b],h_list[a-1])


for i in range(1,n+1):
    if h_list[i-1] > max_list[i]:
        ans += 1

print(ans)
