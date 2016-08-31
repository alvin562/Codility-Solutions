# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    
    values = [False for i in range(X)]
    
    totalValues = 0
    
    for i in range(len(A)):
        
        # if we find a value between 1 and X and hasn't already
        # been represented in our values array then update values
        # array accordingly
        if 1 <= A[i] <= X and values[A[i]-1] == False:
            
            values[A[i]-1] = True
            totalValues += 1
            
        if totalValues == X:
            
            return i
        
    return -1
