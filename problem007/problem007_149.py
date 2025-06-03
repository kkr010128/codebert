n=input()

fn_first=1
fn_second=1

if n >= 2:
    for x in xrange(n-1):
        tmp = fn_first
        fn_first = fn_first + fn_second
        fn_second = tmp

print fn_first