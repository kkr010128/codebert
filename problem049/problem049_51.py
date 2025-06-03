while True:
        x,y = map(int,raw_input().split())
        if x==0:
            break
        else:
            for i in xrange(x):
                print y*"#"
            print ""