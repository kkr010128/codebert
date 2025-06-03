# coding: utf-8

kind, choose = map(int, input().split())
count = 0
total = 0

num = input().split(" ")
for i in num:
    total += int(i)

ok = total / (4 * choose)

for i in num:
    if int(i) >= ok:
        count += 1

if count >= choose:
    print("Yes")
else:
    print("No")