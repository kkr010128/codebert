s = input()
suffix = ''
if s.endswith('s'):
    suffix = 'es'
else:
    suffix = 's'

print(s + suffix)