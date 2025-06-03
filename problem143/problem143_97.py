break_line = int(input())
word = input()

if len(word) <= break_line:
    print(word)
else:
    print('{}...'.format(word[:break_line]))