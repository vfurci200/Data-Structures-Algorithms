#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:57:05 2020

@author: vince
"""

# Uses python3
import sys


#SLOW
# def dict_play(a,x):
    
#     T = dict()
#     T = {a: [] for a in range(len(a))} 
#     Ti = dict(zip(T,a))
#     key_list = list(Ti.keys()) 
#     val_list = list(Ti.values()) 
#     if x in val_list :
#         idx = key_list[val_list.index(x)]
#         return idx
#     else:
#         return -1
    
def binary_search(a,low,high, x):
    
    # write your code here
    if high<low:
        return -1
    mid = round(low + (high-low)/2)
    if x== a[mid]:
        return mid
    if x > a[mid]:
        return binary_search(a,mid+1,high, x)
    if x < a[mid]:
        return binary_search(a,low,mid-1, x)
        
    




def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [5, 1, 2, 3, 4, 5 , 5, 1, 2, 3, 4, 5]
    # data = [5, 1, 5, 8, 12, 13 , 5, 8, 1, 23, 1, 11]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    left, right = 0, len(a)-1
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,left,right, x), end = ' ')
