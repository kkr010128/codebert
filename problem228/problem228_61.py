h = int(input())

cnt = 0
for i in range(h.bit_length()):
    cnt += 2**i
print(cnt)