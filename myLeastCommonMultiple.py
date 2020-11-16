#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:09:23 2020

@author: vince
"""

# Uses python3
import sys
import numpy as np

def gcd_Euclid(a, b):

    if b == 0:
        return a
    a_prime = np.remainder(a,b)
    return gcd_Euclid(b,a_prime)

def least_common_multiple(gdc_res,a,b):
    if a ==0 or b == 0:
        return 0
    least_multiple = a * (b/gdc_res)
    return int(least_multiple)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    gdc_res = gcd_Euclid(a, b)
    print(least_common_multiple(gdc_res,a,b))
