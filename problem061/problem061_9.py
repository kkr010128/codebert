def convert(s):
    o = ord(s)
    if o >= 65 and o <= 90:
        return s.lower()
    elif o >= 97 and o <= 122:
        return s.upper()
    return s


def main():
    strings = input()
    answer = ""
    for s in strings:
        s = s
        answer += convert(s)
    print(answer)

if __name__ == "__main__":
    main()