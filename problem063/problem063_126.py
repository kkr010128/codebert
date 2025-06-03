def main():
    S = ''
    while True:
        try:
            S = S + input()
        except:
            break

    s = S.lower()
    for i in range(97, 123):
        c = chr(i)
        n = s.count(c)
        print('{} : {}'.format(c, n))

main()