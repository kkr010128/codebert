N = int(input())
abc_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
abc = ''
while(N>26):
    n = N%26
    N = N//26
    if n==0:
        abc+=abc_list[25]
        N = N-1
    else:
        abc+=abc_list[n-1]
abc+=abc_list[N-1]
print(abc[::-1])