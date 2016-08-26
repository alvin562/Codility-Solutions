# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):
    # write your code in Python 2.7
    
    a = 1 if A % K == 0 else 0
    
    return B/K - A/K + a
