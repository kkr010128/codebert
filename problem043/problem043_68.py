while True:
    line = list(map(int, input().split()))
    if line==[0,0]: break
    print(' '.join(map(str,sorted(line))))