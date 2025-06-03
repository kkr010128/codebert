ring_str=input()
key=input()

ring_str+=ring_str

if key in ring_str:
    print('Yes')
else:
    print('No')
