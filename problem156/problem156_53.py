N = int(input())

# 以下がとてもわかりやすい
# https://drken1215.hatenablog.com/entry/2020/06/20/231600

for i in range(-200, 200, 1):
    for j in range(-200, 200, 1):
        if i ** 5 - j ** 5 == N:
            print(f'{i} {j}')
            exit(0)