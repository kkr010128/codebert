alpha = "abcdefghijklmnopqrstuvwxyz"
A = [0]*26

while True :
    try :
        n = input()
        
        for i in range(len(n)) :
            if n[i] in alpha or n[i].lower() in alpha :
                A[alpha.index(n[i].lower())] += 1
    except :
        break
    
for j in range(len(A)) :
    print(alpha[j], ":", A[j])
