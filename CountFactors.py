# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import math

def solution(N):
    # write your code in Python 2.7
    
    answer = 0  # number of factors of N initially set to 0
    
    sqrtN = int(math.sqrt(N))   # the floored value of square root of N
    
    # we loop through all values less than sqrtN
    # and check if they divide N evenly
    for i in range(1, sqrtN+1):
        
        # if N is divisible by i then we have two cases
        if N % i == 0:
            
            # N divided by i equals i 
            # in this case we only count the factor once
            if N/i == i:
                
                answer += 1
            
            # else N divided by i does not equal i
            # so we count two factors
            else:
                
                answer += 2
                
    return answer
