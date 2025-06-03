n, k = map(int, input().split())
a = list(map(int, input().split()))

answers = []
for i in range(k, n):
    answers.append(a[i-k] < a[i])
for ans in answers:
    if ans:
        print("Yes")
    else:
        print("No")
