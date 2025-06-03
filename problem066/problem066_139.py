while True:
    st = list(raw_input())
    if st[0] == '-':
        break
    m = int(raw_input())
    for k in range(m):
        h = int(raw_input())
        st = st + st[:h]
        del st[:h]
    print ''.join(st) 