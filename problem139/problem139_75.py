H1,M1,H2,M2,K = map(int,input().split())

M_all = (H2 *60 + M2) - (H1 *60 + M1) - K

if M_all <= 0:
    print('0')
else:
    print(M_all)