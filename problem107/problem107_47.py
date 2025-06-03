def resolve():
  N = int(input())
  X = input()

  if N == 1:
    if X.count("1"):
      print(0)
    else:
      print(1)
    return True

  base_1_count = X.count("1")
  if base_1_count == 0:
    for _ in range(N):
      print(1)
    return True

  X_int = int(X, 2)
  X_int_p = X_int%(base_1_count + 1)

  # RE 対策
  if base_1_count == 1:
    for i in range(N):
      if X[i] == "1":
        print(0)
      else:
        if i == N - 1:
          Xi = X_int_p + 1
        else:
          Xi = X_int_p
        count = 1
        while Xi != 0:
          Xi %= bin(Xi).count("1")
          count += 1
        print(count)
    return True

  X_int_m = X_int%(base_1_count - 1)
  for i in range(N):
    # 初期値計算を高速にやる
    if X[i] == "1":
      temp_1_count = base_1_count-1
      pow_2 = pow(2, N-i-1, base_1_count-1)
      if X_int_m <= pow_2:
        Xi = X_int_m - pow_2 + base_1_count-1
      else:
        Xi = X_int_m - pow_2
    else:
      temp_1_count = base_1_count+1
      Xi = X_int_p + pow(2, N-i-1, base_1_count+1)
      while Xi >= base_1_count+1:
        Xi %= base_1_count+1

    # print("1_c={0}".format(temp_1_count))
    if temp_1_count == Xi:
      print(1)
      continue

    count = 1
    while Xi != 0:
      num_of_1 = bin(Xi).count("1")
      Xi %= num_of_1
      count += 1
    print(count)

if __name__ == "__main__":
    resolve()