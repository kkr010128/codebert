if __name__ == "__main__":
    T = input()
    ans = T
    ans = ans.replace("P?", 'PD')
    ans = ans.replace("??", 'PD')
    ans = ans.replace("?D", 'PD')
    ans = ans.replace("?", 'D')
    print(ans)