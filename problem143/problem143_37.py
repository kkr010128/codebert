k = int(input())
s = input()

if k >= len(s):
    print(s)
else:
    print(f"{s[:k]}...")