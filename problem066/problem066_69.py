while 1:
    w=raw_input()
    if w=='-': break
    n=int(raw_input())
    for i in range(n):
        l=int(raw_input())
        w=w[l:]+w[:l]
    print w