#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:06:29 2020

@author: vince
"""


import sys
import numpy as np

def get_fibonacci_last_digit(n):
    if (n < 1):
        return n

    prev = 0
    curr = 1

    for _ in range(n - 1):
        prev, curr = curr % 10, (prev + curr) % 10

    return curr % 10

def get_fibonacci_sum_squares(n):
    # Little trick:
    # Pisano period modulo 10 is 60
    vertical_side = get_fibonacci_last_digit(n % 60)
    horizontal_side = get_fibonacci_last_digit((n + 1) % 60)
    return (vertical_side * horizontal_side) % 10
        
if __name__ == '__main__':
    n = int(input())
    # n = 73
    print(get_fibonacci_sum_squares(n))