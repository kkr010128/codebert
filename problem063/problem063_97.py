import sys
line = sys.stdin.read().lower()
al_dict = {}

for al in [chr(i) for i in range(ord('a'), ord('z')+1)]:
    al_dict[al] = 0
    
for al in line:
    if al_dict.get(al) != None:
        al_dict[al] += 1

for al in al_dict:
    print('{} : {}'.format(al, al_dict[al]))
