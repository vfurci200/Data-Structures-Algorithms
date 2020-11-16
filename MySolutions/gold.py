# Uses python3
import sys
import time



def optimal_weight(W, w):
    # write your code here
    start_time = time.time()
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
        
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return result


def optimalSolution(capacity, items):
    start_time = time.time()
    n = len(items)
    i = n
    w = capacity
    used_items = []
    if sum(items) <= capacity:
        return w
    else:
        while i>0 and w>0:
            if items[i] == items[i-1]:
                i=i-1
            else:
                used_items.append(i - 1)
                w = w - items[i - 1]
                i = i - 1
            
            
            
                # while i > 0 and w > 0:
                #     if T[i][w] == T[i - 1][w]:
                #         i = i - 1
                #     else:
                #         used_items.append(i - 1)
                #         w = w - items[i - 1]
                #         i = i - 1
    print("--- %s seconds ---" % (time.time() - start_time))
    return used_items

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    W = 10
    n = 3
    w = [1,4,8]
    print(optimal_weight(W, w))
    print(optimalSolution(W, w))
