import numpy as np
list_data = [int(x) for x in input().split(" ")]

print(np.ceil(list_data[0] / list_data[1]).astype(int) * list_data[2])