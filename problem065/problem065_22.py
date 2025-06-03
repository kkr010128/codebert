key = raw_input().upper()
c = ''
while True:
    s = raw_input()
    if s == 'END_OF_TEXT':
        break
    c = c + ' ' + s.upper()
   
cs = c.split()
total = 0
for w in cs:
    if w == key:
        total = total + 1
        
print total