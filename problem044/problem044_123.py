
def havediv( target, elm):
    s = target / elm
    if target == s*elm:
        return True
    else:
        return False


if __name__ == "__main__":
        v = map( int, raw_input().split())
        ct = 0
        i = v[0]
        while i <= v[1]:
            if havediv( v[2], i):
                ct += 1
            i += 1
        print ct