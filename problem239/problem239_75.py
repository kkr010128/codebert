c = str(input())
a = 'abcdefghijklmnopqrstuvwxyz'
for i, letter in enumerate(a):
    if c == letter:
        ans = a[i+1]
print(ans)