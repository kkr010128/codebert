def main():
    K = int(input())
 
    work = 7
 
    answer = -1
    for i in range(1, K+1):
        i_mod = work % K
        if i_mod == 0 :
            answer = i
            break
        work = i_mod * 10 + 7
    print(answer)
main()