import re

def find_a_word(w, t):
    list = []
    for e in map(lambda x: re.split(r'\s|,|\.', x.lower()), t):
        list.extend(e)
    return list.count(w.lower())

if __name__ == '__main__':
    w = input()
    t = []
    while True:
        i = input()
        if i == 'END_OF_TEXT':
            break
        else:
            t.append(i)

    print(find_a_word(w, t))

