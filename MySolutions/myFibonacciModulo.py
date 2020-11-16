#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:36:49 2020

@author: vince
"""

# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
    
    period_len = pisanoPeriod(m)
    n = n % period_len
    
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current = current, previous + current
         
    return (current % m)


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # # n = 239
    # # m = 1000
    # # n = 2015
    # # m = 3
    # n = 14
    # m = 3
    

    print(get_fibonacci_huge(n, m))
