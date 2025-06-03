def resolve():
    K = int(input())
    S = input()
    if K < len(S):
        print(S[:K] + "...") 
    else:
        print(S)
resolve()