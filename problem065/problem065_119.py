target_word = raw_input()
text = ''
while True:
    raw = raw_input()
    if raw == "END_OF_TEXT":
        break
    # text += raw.strip('.') + ' '
    text += raw + ' '

# ans = 0
print(text.lower().split().count(target_word))
# for word in text.lower().split():
#     if word == target_word:
#         ans += 1
# print(ans)