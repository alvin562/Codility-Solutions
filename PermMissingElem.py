# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    N = len(A)+1    # A consists of integers in range [1, N]
    
    answer = N*(N+1)/2   # sum of integers from 1 to N
    
    # we subtract each number in A from answer
    # the final result will be the missing 
    # element in A
    for i in range(len(A)):
        
        answer -= A[i]
        
    return answer
