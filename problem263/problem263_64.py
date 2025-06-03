n = int(input())
A = list(map(int, input().split()))

cumsum = [[0 for j in range(2)] for i in range(60)]
ans = [0] * 60
#print(cumsum)

for i in range(len(A) - 1, -1, -1):
    plus_num = A[i]
    bit_num = format(plus_num, "060b")
    #print(bit_num)
    for i, bit in enumerate(bit_num):
        bit = int(bit)
        if bit == 0:
            ans[i] += cumsum[i][1]
        else:
            ans[i] += cumsum[i][0]
        cumsum[i][bit] += 1
    #print(ans)
    #print(cumsum)

ans_num = 0
mod = 10**9 + 7
for i, cnt in enumerate(ans):
    ans_num += 2**(59-i) * cnt
    ans_num %= mod
print(ans_num)

