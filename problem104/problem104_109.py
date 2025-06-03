L, R, d = map(int, input().split())

if L%d==0:
    st = L
else:
    st = (L//d+1)*d

count = 0
for i in range(st, R+1, d):
    if i <= R:
        count += 1
    else:
        break
print(count)