# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    for i in range(len(A)):
        
        A[i] = abs(A[i])
        
    A = set(A)
    
    return len(A)
            
