text = input()
times = int(input())

for i in range(times):
    function = input().split()
    word = text[int(function[1]):int(function[2])+1]

    if function[0] == "print":
        print(word)

    elif function[0] == "reverse":
        word_reverse = word[::-1]
        text = text[:int(function[1])] + word_reverse + text[int(function[2])+1:]

    elif function[0] == "replace":
        text = text[:int(function[1])] + function[3] + text[int(function[2])+1:]