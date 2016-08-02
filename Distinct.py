# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
    


def quickSort(A, start, end):
    
    if start >= end:
        return
    
    wall = start - 1    # we place the wall one position behind the start
    curr = start        # position of current element is initially pointing to start
    pivot = A[end]      # our pivot is always the last element
    
    while curr < end:
        
        # if the current element is less than the pivot
        # then we swap it with the element to the right
        # of the wall and move wall up one spot
        if A[curr] < pivot:
            
            temp = A[wall+1]
            A[wall+1] = A[curr]
            A[curr] = temp
            
            wall += 1
        
        curr += 1
    
    # finally we swap the pivot with the
    # element just to the right of the wall
    temp = A[wall+1]
    A[wall+1] = A[end]
    A[end] = temp
    
    # quicksort left and right halves of array
    quickSort(A, start, wall)
    quickSort(A, wall+2, end)
        
            

def solution(A):

    if len(A) <= 1:
        return len(A)

    quickSort(A, 0, len(A)-1)
    
    distinctNumbers = []
    distinctNumbers.append(A[0])
    total = 1
    
    for i in range(1, len(A)):
        
        previousNumber = distinctNumbers[i-1]
        
        if previousNumber != A[i]:
                
            total += 1
        
        distinctNumbers.append(A[i])
        
    return total
