# B - Battle

# 入力 A B C D
A, B, C, D = map(int, input().split(maxsplit=4))

while True:
    C -= B
    if C <= 0:
        answer = 'Yes'
        break

    A -= D
    if A <= 0:
        answer = 'No'
        break

print(answer)
