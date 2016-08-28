# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    # array of boolean values representing 
    # whether the positive integer occurs in A
    # (e.g. A[0] = 1 if 1 is in A, A[1] = 0 if 
    # 2 is not in A)
    values = [0 for i in range(len(A))]
    
    for i in range(len(A)):
        
        # if the value is positive and within the range 
        # [1, number of values in A] then we mark it in 
        # our values array
        if A[i] > 0 and A[i] <= len(A):
            
            values[A[i]-1] = 1
    
    # next we loop through the values in values
    # and as soon as we find a value 0, then the
    # index of that value + 1 is our answer
    for i in range(len(values)):
        
        if values[i] == 0:
            
            return i+1
    
    # else all values in values are marked 1 meaning 
    # the minimal positive integer is len(values)+1
    return len(values)+1
