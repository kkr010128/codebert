word = raw_input()
text = []
while True:
    raw = raw_input()
    if raw == "END_OF_TEXT":
        break
    text += raw.lower().split()

print(text.count(word))
# print(text.lower().split().count(word))