N = int(input())
st = []
for _ in range(N):
    s,t = map(str,input().split())
    st.append((s,int(t)))
X = input()

ans = 0
flag = False
for s,t in st:
    if flag:
        ans += t
    if s == X:
        flag = True

print(ans)