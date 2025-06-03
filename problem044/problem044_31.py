i = list(map(int, input().split()))
a = i[0]
b = i[1]
c = i[2]

answer = 0

for j in range(a, b + 1) :
    if c % j == 0 :
        answer += 1
print(answer)