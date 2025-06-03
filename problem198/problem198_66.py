N = int(input())
string = [0 for i in range(N)]
calc_str = lambda :"".join(list(chr(i+ord('a')) for i in string))
chr_a = ord('a')
print(calc_str())
now = N-2


while N > 1:
    if string[now+1]-max(string[:now+1]) > 0:
        if now == 0: break
        string[now+1] = 0
        now -= 1
        
    else:
        string[now+1] += 1
        now = N-2

        print(calc_str())