#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:57:49 2020

@author: vince
"""

# python3
import sys
import numpy as np


def compute_min_refills(distance, tank, stops):
    # write your code here
    m = np.array([tank])
    s_stops = np.sort(stops)
    m_run = np.array([0])
    m_run_to_empty = np.array([0])
    max_stop = 0
    i,j = 0,0
    if np.size(s_stops) <= 1:
        if m > distance:
            return 0
        if m >= s_stops[i] and m+s_stops[i]>= distance:
            m_run[j] = s_stops[i]
            i = i + 1
            return 1
        else:
            return -1
            
    while  m_run.sum() + m < distance:
        a = m >= s_stops 
        a = np.where(a == True)[0]
        if np.size(a)>0:
            m_run = np.append(m_run,[s_stops[a[-1]]],axis =0)
            # m_run_to_empty = np.array(m_run)
            # m_run_to_empty = np.append(m_run,[m[0]],axis =0)
            last_stop = s_stops[a[-1]]
            s_stops = s_stops[a[-1]+1:]
            s_stops = s_stops - last_stop
            j = j + 1
        else:
            return -1
    return j
    
    
    


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    
    # d = 10
    # m = 0
    # _ = 4
    # stops = [100, 200,300,400]
    # d = [10]
    # m = [3]
    # _ = [4]
    # stops = [1,2,5,9]
    print(compute_min_refills(d, m, stops))
