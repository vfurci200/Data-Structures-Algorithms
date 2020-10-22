#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:27:07 2020

@author: vince
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:07:18 2020

@author: vince
"""

# Uses python3
def calc_fib_last_digit(n):
    array = [None] * (n + 1)
    array[0] = 0
    if n >= 1:
        array[1] = 1
        for i in range(2,n+1):
            array[i] = array[i-1]%10 + array[i-2]%10
            
    return(array[-1]) %10   
        
n = int(input())
print(calc_fib_last_digit(n))
