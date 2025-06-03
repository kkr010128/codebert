n = int(input())
dict = set()
for _ in range(n):
    c, s = input().split()
    if c == 'insert':
        dict.add(s)
    else:
        print(('no', 'yes')[s in dict])



