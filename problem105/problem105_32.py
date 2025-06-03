N = int(input())
a = list(map(int, input().split()))


answer = 0
for i, e in enumerate(a):
    i += 1
    if i % 2 != 0 and e % 2 != 0:
        answer += 1 
print(answer)