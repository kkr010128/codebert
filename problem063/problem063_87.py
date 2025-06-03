def main():

    alphabets_table = [0 for i in range(26)]

    while True:
        try:
            input_string = input()
            lower_string = input_string.lower()
            for i, _letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
                alphabets_table[i] += lower_string.count(_letter)
        except EOFError:
            break
            
    for i, _letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
        print('%s : %s' % (_letter, alphabets_table[i]))


main()