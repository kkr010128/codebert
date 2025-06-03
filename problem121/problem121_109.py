n = int(input())
ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1,15):
    if n<=26**i:
        order=i
        n-=1
        break
    n-=26**i

for i in range(order):
    print(ascii_letters[n//(26**(order-i-1))],end='')
    n%=(26**(order-i-1))
print()