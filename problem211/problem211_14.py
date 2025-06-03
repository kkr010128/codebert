mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    N, R = [int(x) for x in raw_input().split()]
    
    if N >= 10:
      print(R)
    else:
      print(R + ((10 - N) * 100))
    
    

main()