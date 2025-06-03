def main():
    N = int(input())
    shougen = []
    for _ in range(N):
        A = int(input())
        shougen.append([list(map(int, input().split())) for _ in range(A)])
    
    ans = 0
    for i in range(2**N):
        state = [1]*N
        
        for j in range(N):
            if (i >> j) & 1:
                state[j] = 0
        
        flag = True
        for k in range(N):
            if not flag:
                break
            if state[k] == 1:
                for ele in shougen[k]:
                    if state[ele[0]-1] != ele[1]:
                        flag = False
                        break
                    
        if flag:
            ans = max(ans, sum(state))
    
    print(ans)
                
    
if __name__  == '__main__':
    main()