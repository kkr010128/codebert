while True:
    exp = input()
    if '?' in exp: break
    print('%d' % (int(eval(exp))))