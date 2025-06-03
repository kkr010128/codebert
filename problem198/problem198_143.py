n = int(input())

buf = [0]*n

def solv(idx,char):
    aida = n - idx
    if idx == n:
        print("".join(buf))
        return

    for i in range(char + 1):
        buf[idx] = chr(ord('a') + i)
        solv(idx+1,max(i + 1,char))

solv(0,0)