# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    
    # write your code here
    packed_v = [0]
    c_left= capacity
    weights = np.array(weights)
    values = np.array(values)
    valueOweight = values / weights
    while c_left != 0:
        mvp = np.amax(valueOweight)
        idx_mvp_ = np.where(valueOweight == mvp)[0]
        idx_mvp = idx_mvp_[0]
        if c_left - weights[idx_mvp] >= 0:
            packed_v = packed_v + values[idx_mvp]
            c_left = c_left - weights[idx_mvp]
            valueOweight[idx_mvp] = 0
            if np.sum(valueOweight)==0:
                c_left = 0
        else:
            fract = c_left / weights[idx_mvp]
            packed_v = packed_v + (values[idx_mvp]* fract)
            c_left = 0
            
        
    return packed_v[-1]


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split())) 
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    
    # n, capacity = [3,50] 
    # values =  [60,100,120]
    # weights = [20,50,30]
    
    # n, capacity = [1,1000] 
    # values =  [500,500]
    # weights = [30,30]
    
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
