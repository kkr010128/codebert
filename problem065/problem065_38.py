search_s = input()
cnt = 0
while True:
    s = input()
    if s == "END_OF_TEXT": break
    word_list = s.lower().split()
    for word in word_list:
        if word == search_s:cnt += 1

print(cnt)