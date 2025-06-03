if __name__ == '__main__':
    try:
        s = str(input())
        s.lower()
        if s[len(s)-1] != 's':
            s += 's'
            print(s)
        else:
            s += 'es'
            print(s)
    except Exception:
        pass