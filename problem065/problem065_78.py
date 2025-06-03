if __name__ == '__main__':
    W = input().lower()
    words = []
    while True:
        line = input()
        [words.append(i) for i in line.lower().split()]
        if 'END_OF_TEXT' in line: break
    print(words.count(W))