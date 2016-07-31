# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# this solution can be done in O(1) space
# my solution uses O(n) space since I chose
# not to rotate the array in place

def solution(A, K):
    
    arrSz = len(A)
    answer = []
    
    # rotating the array K times in this 
    # case results in the same array
    if arrSz == 0 or K % arrSz == 0:
        
        return A
        
    # rotating the array K times when
    # K is greater than the size of 
    # array is the same as rotating
    # it K % arrSz times
    if K > arrSz:
        
        K %= arrSz
        
    for i in range(arrSz-K, arrSz):
        
        answer.append(A[i])
        
    for i in range(0, arrSz-K):
        
        answer.append(A[i])
        
    return answer
