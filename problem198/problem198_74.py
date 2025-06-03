def f(num,N,S):
    alphabet = ["a","b","c","d","e","f","g","h","i","j"]
    if N == num:
        for i in range(len(S)):
            print(S[i])
        return
    else:
        tmp = []
        length = len(S)
        for i in S:
            ttmp = sorted(list(i))
            for j in range(alphabet.index(ttmp[-1])+2):
                tmp.append(i+alphabet[j])
        f(num+1,N,tmp)
 
N = int(input())
f(1,N,["a"])