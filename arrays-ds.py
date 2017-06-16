#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
s = str(arr[::-1])
s = s.strip("[]")
s = s.replace(',', '')
print(s)
