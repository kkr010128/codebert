while True:
    n = input();
    if n == '-':
        break;
    m = int(input());
    N = list(n);
    
    for i in range(0,m):
        h = int(input());
        for j in range(0,h):
            x = [];
            x.append(N[0]);
            N.pop(0);
            N.append(x[0]);
    print(''.join(N));
