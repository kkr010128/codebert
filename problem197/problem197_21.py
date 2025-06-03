a,b,c=map(int,raw_input().split())
if a+b >= c:
    print "No"
else:
    ans1 = 4 * a * b;
    ans2 = (c - a - b) * (c - a - b)
    if ans1 < ans2:
        print "Yes"
    else:
        print "No"