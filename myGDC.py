#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:45:25 2020

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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # a = 3
    # b = 27
    print(gcd_Euclid(a, b))
