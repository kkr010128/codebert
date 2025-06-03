a = input()

alp = [chr(i) for i in range(ord('a'),ord('z')+1)]

if a in alp:
    print('a')
else:
    print('A')