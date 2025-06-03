s = input()
a = int((len(s)-1)/2)
b = int((len(s)+3)/2)
r = ''.join(reversed(s[b-1:]))
if s[:a]== s[:a:-1] and s[b-1:]== r:
    print('Yes')
else:
    print('No')