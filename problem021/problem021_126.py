def main():
    S = input()
    stack1, stack2 = [], []
    
    sum = 0
    N = len(S)
    for i in range(N):
        if S[i] == "\\":
            stack1.append(i)
        elif S[i] == "/" and stack1:
            j = stack1.pop()
            tmp = i - j
            sum += tmp
            
            while stack2 and stack2[-1][0] > j:
                tmp += stack2.pop()[1]
            stack2.append([j, tmp])
            
    print(sum)
    print(len(stack2), *[a for j, a in stack2])
    

if __name__=="__main__":
    main()
