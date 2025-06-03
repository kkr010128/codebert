N = int(input())
tax_min = int(N*0.08/1.08)
tax_max = int((N+1)*0.08/1.08)
if tax_min != tax_max:
    print(":(")
else: print(N - tax_min)