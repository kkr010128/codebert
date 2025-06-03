al = "abcdefghijklmnopqrstuvwxyz"
k  = int(input())
def dfs(s: "char", i):
    if(len(s)==k):
        print(s)
    else:
        for j in range(i+1):
            if al[j]==al[i]:
                dfs(s+al[j], i+1)
            else:
                dfs(s+al[j], i)




def main():
    #sの後ろを変えていくdfs
    dfs("", 0)


if __name__ == '__main__':
    main()
