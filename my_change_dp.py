# Uses python3
import sys
import numpy as np

def get_change(money,coins):
    #write your code here
    min_num_coins = [float("inf")]*(money+1)
    min_num_coins[0] = 0
    for m in range(1,money+1):
        for i in range(0,len(coins)):
            if m >= coins[i]:
                numCoins = min_num_coins[m-coins[i]]+1
                if numCoins < min_num_coins[m]:
                    min_num_coins[m] = numCoins
                    
    return min_num_coins[money]
    





if __name__ == '__main__':
    m = int(sys.stdin.read())
    
    coins = [1,3,4]
    print(get_change(m,coins))
