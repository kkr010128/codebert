H1,M1,H2,M2,K = map(int, open(0).read().split())
diff = (H2-H1) * 60 + (M2-M1)
print(diff-K)