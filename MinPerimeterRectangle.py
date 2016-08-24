# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


import math

def solution(N):

    sqrtN = int(math.sqrt(N))+1
    minPerimeter = 1000000000
    
    # to generate all the possible perimeters
    # we only need to look at side lengths less
    # than or equal to sqrt(N)
    for i in range(1, sqrtN):
        
        if N % i == 0:
            
            A = i
            B = N/i
            perimeter = 2*(A+B)
            
            if perimeter < minPerimeter:
                
                minPerimeter = perimeter
    
    return perimeter
