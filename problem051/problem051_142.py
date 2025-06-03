while True:
    H, W = map(int, raw_input().split())
    if H == 0 or W == 0:
        break
    even_line = ''
    odd_line  = ''
    for i in xrange(W):
        if i % 2 == 0:
            even_line = even_line + '#'
            odd_line = odd_line + '.'
        else:
            even_line = even_line + '.'
            odd_line = odd_line + '#'
    for i in xrange(H):
        if i % 2 == 0:
            print even_line
        else:
            print odd_line
    print ''