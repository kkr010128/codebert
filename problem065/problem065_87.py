def make_text():
    temp = []
    while True:
        row = input().split()
        if row == ['END_OF_TEXT']:
            break
        temp.append(list(map(lambda x: x.lower(), row)))
    return temp

def find_word(word,text):
    num = 0
    for row in text:
        for t in row:
            if t == word:
                num += 1

    return num

if __name__ == '__main__':
    w = input()
    t = make_text()
    num = find_word(w,t)
    print(num)
