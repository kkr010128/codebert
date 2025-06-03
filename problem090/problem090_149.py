def main(S):
    rains = S.split('S')
    return max([len(r) for r in rains])

if __name__ == '__main__':
    S = input()
    ans = main(S)
    print(ans)
    
