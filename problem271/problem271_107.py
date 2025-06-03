n = int(input())
s = input()

ans = ''
for c in s:
    nc_ord = ord(c) + n
    while nc_ord > ord('Z'):
        nc_ord -= 26
    ans += chr(nc_ord)
print(ans)
