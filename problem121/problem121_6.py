n = int(input())

def calc(m, res):
        q, mod = divmod(m, 26)
        if (mod == 0):
            q = q - 1
            mod = 26
            res = chr(ord("a") + (mod - 1)) + res
        else:
            res = chr(ord("a") + (mod - 1)) + res
        if (q > 0):
            calc(q, res)
        else:
            print(res)
        return
    
calc(n, "")