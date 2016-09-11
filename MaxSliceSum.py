# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


# Kadane's algorithm scans the array, computing at
# each position the maximum subarray ending in that 
# position.  At every position, the Kadane's algorithm
# updates the global maximum subarray.
def solution(A):

    global_max = curr_max = A[0]
    
    for i in range(1, len(A)):
        
        curr_max = max(A[i], curr_max+A[i])
        global_max = max(curr_max, global_max)
        
    return global_max
