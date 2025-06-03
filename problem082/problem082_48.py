# coding: utf-8

def main():
    s = input()
    t = input()

    ans = len(t)
    
    for i in range(len(s) - len(t) + 1):
        a = s[i:i+len(t)]
        # print(a, t)
        ans_list = [1 for x, y in zip(a, t) if x!=y]
        tmp_ans = sum(ans_list)
        ans = min(ans, tmp_ans)
        
        if ans == 0:
            break
        
    print(ans)
    
        

main()