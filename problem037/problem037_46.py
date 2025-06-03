#! /usr/bin/env python
# -*- coding: utf-8 -*-

raw_time = int(raw_input())

if 0 <= raw_time < 86400:
    hour = raw_time / 3600
    minute = (raw_time - hour * 3600) / 60
    second = (raw_time - hour * 3600 - minute * 60)
    print("%d:%d:%d") % (hour, minute, second)