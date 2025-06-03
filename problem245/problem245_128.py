N = int(input())
print(input().count("ABC"))

""" 3文字ずつスライスし判定
S = input()
count = 0
# スライスでi+2文字目まで行くのでfor文範囲はN-2でとどめる
for i in range(N-2):
    if S[i:i+3] == "ABC":
        count += 1
print(count) """