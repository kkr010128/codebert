# Function for calc
def match(n, a, b):
    if (b - a)% 2 == 0:
        print((b-a)/2)
    else:
        if (n - b) >= a:
            print((a)+((b-(a+1))/2))
        else:
            x=(n-b+1)
            print(x+((n-(a+x))/2))
# Run match
in_string = raw_input()
[N, A, B] = [int(v) for v in in_string.split()]
match(N, A, B)
