#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:49:24 2020

@author: vince
"""

# Uses python3


import sys

def fibonacci_sum_last_digit_partial(to_,from_):

    if from_ == to_:
        return calc_fib_last_digit(from_)
    else:
        from_ %= 60
        to_ %= 60

        from_last = get_fibonacci_huge(from_ + 1, 10) - 1
        to_last = get_fibonacci_huge(to_ + 2, 10) - 1

    return (to_last - from_last) % 10

def get_fibonacci_huge(n, m):
    period_len = pisanoPeriod(m)
    n = n % period_len
    return get_fibonacci(n)%m
    
def get_fibonacci(n):
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current = current, previous + current
         
    return (current)
        
def calc_fib_last_digit(n):
    array = [None] * (n + 1)
    array[0] = 0
    if n >= 1:
        array[1] = 1
        for i in range(2,n+1):
            array[i] = array[i-1]%10 + array[i-2]%10
            
    return(array[-1])  

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
    # m = 1
    # n = 2
    print(fibonacci_sum_last_digit_partial(n,m))
