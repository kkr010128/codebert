word = input()

word_len = len(word)

if word[word_len-1] == 's':
  print(word + 'es')
else:
  print(word + 's')