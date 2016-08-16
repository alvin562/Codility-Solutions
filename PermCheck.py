# you can write to stdout for debugging purposes, e.g.
#print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    # array of boolean values 
    # 1 if value occurs in array A; 0 otherwise
    inArray = [0 for i in range(len(A))]    
    
    for i in range(len(A)):
        
        value = A[i]
        
        # return 0 if A contains value greater than N
        if value > len(A):
            
            return 0
        
        # if the value is not in the array then set inArray[value-1] to 1
        if inArray[value-1] == 0:
            
            inArray[value-1] = 1
            
        # else we return 0 because the value occurs twice
        else:
            
            return 0
        
    # lastly we check if all the values in inArray is 1    
    for i in range(len(A)):
        
        if inArray[i] == 0:
            
            return 0
            
    return 1
