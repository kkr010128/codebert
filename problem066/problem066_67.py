import sys
while True:
    try:
        word = input()
        if word == "-":
            break
        word_len = len(word)
        words_shuffle = []
        
        for i in range(word_len):
            words_shuffle.append(word[i])

        n = int(input())
        for i in range(n):
            h = int(input())
            words_shuffle = words_shuffle[h:] + words_shuffle[:h]

        for i in range(word_len-1):
                print(words_shuffle[i], end="")
        print(words_shuffle[-1])
        
    except EOFError:
        break