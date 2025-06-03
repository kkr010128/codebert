n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

count = 0
for item in t:
    if item in s:
        count += 1
print(count)