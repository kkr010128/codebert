while True:
    word = input()
    if word == '-':
        break

    n = int(input())
    for nc in range(n):
        h = int(input())
        word = word[h:] + word[:h]
    print(word)