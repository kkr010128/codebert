S = input()

length = len(S)
leng = int(length/2)
cnt = 0

for i in range(leng):
    if S[i] == S[length-(i+1)]:
        continue
    else:
        cnt += 1

print(cnt)