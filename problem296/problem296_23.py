import numpy as np
S = input()
K = int(input())
seq = []
init = 1
def seq_count(strings, lst):
    init = 1
    for i in range(len(strings)-1):
        if strings[i] == strings[i+1]:
            init += 1
        else:
            lst.append(init)
            init = 1
    lst.append(init)
seq_count(S, seq)
if S[0] != S[-1]:
    array = np.array(seq)
    ans = array // 2
    print(int(np.sum(ans))*K) 
else:
    seq2 = seq[1:-1]
    array = np.array(seq2)
    part_ans = array // 2
    if len(seq) > 1:
        print(int(np.sum(part_ans))*K+((seq[0]+seq[-1])//2)*(K-1)+(seq[0]//2)+(seq[-1]//2))
    else:
        print((seq[0]*K)//2)