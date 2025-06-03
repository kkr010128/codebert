w = input()
t = []
while True:
    s = [1 if i.lower() == w else 'fin' if i == 'END_OF_TEXT' else 0 for i in input().split()]
    t += s
    if 'fin' in s:
        break
print(t.count(1))
