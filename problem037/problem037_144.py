#!/usr/bin/env python
# -*- coding: utf-8 -*-

var = int(raw_input())

h = str(var / 3600)
ms = var % 3600
m = str(ms / 60)
s = str(ms % 60)

print ":".join([h, m, s])