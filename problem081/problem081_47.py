def dontbelate(D,T,S):
    if T <  D//S:
        return 'No'
    elif T > D//S:
        return 'Yes'
    else:
        if D%S == 0:
            return 'Yes'
        else:
            return 'No'


if __name__ == "__main__":
    D,T,S = map(int, input().split())
    print(dontbelate(D,T,S))