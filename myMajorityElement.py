#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:12:35 2020

@author: vince
"""

# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    a_sorted = quick_sort(a, left, right)
    
    n = right
    i = 0
    while i < n:
        count = 1
        while i < n - 1 and a[i + 1] == a[i]:
            count = count + 1
            i = i + 1
        if count > n / 2:
            return 1
        i = i + 1
    return -1



def quick_sort(a,l,r):
    while l < r:
        m = Partition(a,l,r)
        if (m-l) < (r-m): #if m in bottom half
            quick_sort(a, l, m-1)
            l=m+1
        else:
            quick_sort(a, m+1, r)
            r= m -1
    return a

def Partition(a,l,r):
    x = a[l]
    j = l
    for i in range(l+1,r):
        if a[i]<=x:
            j= j+1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n = 5
    # a = [2,3,9,2, 2]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
