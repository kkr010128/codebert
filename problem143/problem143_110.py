#define S as string
#print S until len is equal to K
#time complexity O(1)

K = int(input())
S = input()

str = S

if len(S) > K:
    print (str[0:K]+ "...")
else:
    print(str)
