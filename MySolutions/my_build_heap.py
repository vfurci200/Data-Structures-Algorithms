# python3


def build_heap(data,n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    i = round(n/2)
    while i >= 0:
        sift_down(data,i,swaps)
        # if newSwaps:
        #     swaps.extend(newSwaps)
        
        i -=1
    return swaps

def sift_down(H,i,swaps):
    maxIndex = i
    n = len(H)
    leftChild = 2*i +1
    rightChild = (2*i) + 2
    # parent = i/2
    
    if leftChild< n and H[leftChild] < H[maxIndex]:
        maxIndex = leftChild
    if rightChild < n and H[rightChild] < H[maxIndex]:
        maxIndex = rightChild
    if i != maxIndex:
        swap = [i, maxIndex]
        swaps.append(swap)
        H[i], H[maxIndex] = H[maxIndex], H[i]
        sift_down(H,maxIndex,swaps)
    return swaps
    
    
def main():
    n = int(input())
    data = list(map(int, input().split()))
    # n = 5
    # data = [5,4,3,2,1]
    assert len(data) == n

    swaps = build_heap(data,n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
