A,V = [int(i) for i in input().split() ]
B,W = [int(i) for i in input().split() ]
T = int(input()) 

print ("YES" if V-W > 0 and abs(A-B) / (V-W) <= T else "NO" ) 
