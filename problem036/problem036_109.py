#! /usr/bin/env python
# -*- coding: utf-8 -*-

height, width = map(int, raw_input().split())
print("%d %d") % (height * width, (height + width) * 2)