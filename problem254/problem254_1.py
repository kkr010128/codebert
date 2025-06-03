A = int(input())
B = int(input())

for i in range(1,4):
    if i == A:
        continue
    elif i == B:
        continue
    else:
        ans = i
        break
print(ans)