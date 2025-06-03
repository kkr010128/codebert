N,A,B = [int(x) for x in input().split()];
#print(A);
#print(B);
#print(N);
#lm = int(A + (B-A-1)/2);
lm = A + (B-A-1)//2;
#print(lm);
#rm = int(N-B+1 + (B-A-1)/2);
rm = N-B+1 + (B-A-1)//2;
#print(rm);
if (B-A)%2 == 0 :
    print((B-A)//2);
else :
    print(min(lm,rm));