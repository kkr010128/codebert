n = int(input())

ans = ""
k = 0
while n // (26**(k)) > 0:
    ans = ans + str(chr(((n-1) % (26**(k+1))+1)//(26**k) + 96))
    n = n - ((n-1) % (26**(k+1))+1)
    k += 1

print(ans[::-1])
