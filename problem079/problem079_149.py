def function(n):
    if n < 3:
        lis.append(0)
    elif 3 <= n < 6:
        lis.append(1)
    else:
        lis.append(lis[n-1] + lis[n-3])
    

def recri(s):
    for n in range(s):
        function(n)

# for n in range(20):
    # print(function(n))
if __name__ == '__main__':
    lis = []
    s = int(input()) + 1
    recri(s)
    print(lis[s-1]%(10 ** 9 + 7))