N = int(input())
amari = N % 1000

if amari == 0:
    change = 0
else:
    change = 1000 - amari

print(change)