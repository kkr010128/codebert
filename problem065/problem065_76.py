target_word = raw_input()
text = ''
while True:
    raw = raw_input()
    if raw == "END_OF_TEXT":
        break
    text += raw.strip('.') + ' '

ans = 0
for word in text.lower().split():
    if word == target_word:
        ans += 1
print(ans)