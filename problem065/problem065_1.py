W = input().lower()
T = ''
 
while True:
    txt = input()
    if txt == 'END_OF_TEXT': break
    T += txt.lower() + ' '
print(tuple(T.split(' ')).count(W))