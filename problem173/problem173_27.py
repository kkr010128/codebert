# ABC162
# FizzBuzz Sum
n = int(input())
ct = 0
for i in range(n + 1):
    if i % 3 != 0:
        if i % 5 != 0:
            ct += i
    else:
        continue

print(ct)