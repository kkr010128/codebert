import sys

def main():
    n,m = map(int, input().split())
    pn_list = [0]*n
    a = [0]*m
    b = [0]*m
    ans_ac = 0
    ans_pn = 0
    pn_list[0]== -1
    
    for i in range (m):
        a[i],b[i]=input().split()
        a[i] = (int(a[i]))
        # print(a[i])
        if pn_list[a[i]-1] != -1:
            if b[i]== "AC":
                ans_pn += pn_list[a[i]-1]
                ans_ac +=1
                pn_list[a[i]-1] = -1 #ペナルティリスト初期化
            else:
                pn_list[a[i]-1] += 1

    print(ans_ac,ans_pn)
    
   
if __name__ == "__main__":
    main()