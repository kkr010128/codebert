n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

result = []
# 
for bit in range(1<<n):
    score = 0
    # 
    for i in range((n)):
        # 
        if bit & (1<<i):
            score += a[i]

    result.append(score)

for m_i in m:
    if m_i in result:
        print('yes')
    else :
        print('no')
