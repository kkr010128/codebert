from collections import Counter
S = input()
S = S[::-1]
# 1桁のmod2019, 2桁の2019, ...
# 0桁のmod2019=0と定めると都合が良いので入れておく
l = [0]
num = 0
for i in range(len(S)):
    # 繰り返し二乗法で累乗の部分を高速化
    # 自分で書かなくてもpow()で既に実装されている
    # 一つ前のmodを利用するとPythonで通せた、それをしなくてもPyPyなら通る
    num += int(S[i]) * pow(10,i,2019)
    l.append(num % 2019)
# print(l)
ans = 0
c = Counter(l)
for v in c.values():
    ans += v*(v-1)//2
print(ans)
