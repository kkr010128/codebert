N = int(input())
answer = 'No'
for i in range(1, 10):
    if N % i == 0:
        sho = N // i
        if sho < 10:
            answer = 'Yes'
            break
print(answer)