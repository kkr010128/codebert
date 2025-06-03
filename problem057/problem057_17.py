def grader(mid, fin, re):
    """ 
    -1 <= mid <= 50
    -1 <= fin <= 50
    0 <= re <= 100

    >>> grader(40, 42, -1)
    'A'
    >>> grader(20, 30, -1)
    'C'
    >>> grader(0, 2, -1)
    'F'
    """
    score = mid + fin 
    if mid == -1 or fin == -1 or score < 30: 
        return 'F' 
    elif score < 50: 
        if re >= 50: 
            return 'C' 
        else:
            return 'D' 
    elif score < 65: 
        return 'C' 
    elif score < 80: 
        return 'B' 
    else:
        return 'A' 


def run():
    while True:
        m, f, r = [int(x) for x in input().split()]

        if m == -1 and f == -1 and r == -1: 
            break
        else:
            print(grader(m, f, r)) 

run()
