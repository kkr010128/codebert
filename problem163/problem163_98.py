s,w=input().split()
s=int(s)
w=int(w)
if s>w:
    print("safe")
if w>s:
   print("unsafe")
if w==s:
   print("unsafe")