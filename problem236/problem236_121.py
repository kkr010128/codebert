#!/usr/bin/env python3
#input
import math
var = [int(input()) for _ in range(3)]
print(math.ceil(var[2]/max(var[0],var[1])))