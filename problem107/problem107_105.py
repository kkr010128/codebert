N = int(input())
X = input()
x = X[::-1]
one = X.count('1')
up = 0
down = 0
for i in range(N):
    up += (int(x[i]) * pow(2,i,one+1) % (one+1))
    up %= one+1
    if one > 1:
        down += (int(x[i]) * pow(2,i,one-1) % (one-1))
        down %= one-1
# print(up,down)
def f(ud,one):
    if one <= 0:
        return 0
    else:
        if ud == 0:
            return 1

        cnt = 0
        while ud != 0:
            ud = ud % one
            one = format(ud,'b').count('1')
            cnt += 1
        return cnt



for i in range(len(X)):
    if X[i] == '1':
        if one > 1:
            print(f((down - pow(2,(len(X)-1) - i, one-1)) % (one-1),one-1))
        #print(down - pow(2,(len(X)-1) - i, one-1) % (one-1))
        else:
            print(0)

    else:
        print(f((up + pow(2,(len(X)-1) - i, one+1)) % (one+1),one+1))
        #print(up + pow(2,(len(X)-1) - i, one+1) % (one+1))
