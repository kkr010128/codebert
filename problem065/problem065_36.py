# coding: utf-8

# ????´¢????±? W
target_word = input()
# ??????
words = []
while (1):
    input_text = input().strip()
    if (input_text == 'END_OF_TEXT'):
        break
    words.extend(input_text.split())

counter = 0
for w in words:
    if (w.lower() == target_word.lower()):
        counter += 1

print(counter)