word = input()

if word[-1] == 's':
    word += 'es'
else:
    word += 's'

print(word)