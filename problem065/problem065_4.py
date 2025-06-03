word = input()
counter = 0
while 1:
 s = input()
 if s == 'END_OF_TEXT':
  break
 else:
  s = list(s.lower().split())
  counter += s.count(word)
  counter += s.count(word + '.')

print(counter)