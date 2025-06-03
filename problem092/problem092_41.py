import numpy as np

inpt = input()
inpt_list = inpt.split(" ")
X, K, D = [int(x) for x in inpt_list]

X_abs = np.abs(X)
num = X_abs // D
rem = K - num
if rem < 0:
    out = X_abs - D*K
else:
    if rem%2==0:
        out = X_abs - num*D
    else:
        out = np.abs(X_abs - num*D - D)
print(out)