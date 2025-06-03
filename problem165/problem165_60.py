n = int(input())
pr = {}
for i in range(n):
    s = input()
    if pr != s:
        pr[s] = True
print(len(pr))
