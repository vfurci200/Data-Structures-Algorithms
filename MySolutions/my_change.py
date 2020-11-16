# Uses python3
import sys
import numpy as np


def get_change(m):
    #write your code here
    coins_den = np.array([5,1,10])
    coins_den = np.sort(coins_den)
    
    m_left = m
    n_coin = 0
    i = 1
    while m_left !=0:
        if m_left - coins_den[-i] >= 0:
            n_coin = n_coin + 1
            m_left = m_left - coins_den[-i]
        else:
            i = i + 1

    return n_coin








if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 2
    print(get_change(m))

