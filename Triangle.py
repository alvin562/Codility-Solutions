# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def swap(A, i, j):
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(A, l, r):
    
    pivot = A[r]
    wall = l
    
    for i in range(l, r):
        
        if A[i] < pivot:
            
            swap(A, i, wall)
            wall += 1
         
    swap(A, wall, r)
    
    return wall


def quicksort(A, l, r):
    
    if l < r:
        
        pivot = partition(A, l, r)
        quicksort(A, l, pivot-1)
        quicksort(A, pivot+1, r)
        
        
def is_triangular(v1, v2, v3):
    
    return v1+v2 > v3 and v1+v3 > v2 and v2+v3 > v1
        

def solution(A):
    # write your code in Python 2.7
    
    N = len(A)
    
    if N < 3:
        
        return 0
        
    quicksort(A, 0, len(A)-1)
    
    p = 0
    q = 1
    r = 2
    
    while p <= len(A)-3:
        
        if is_triangular(A[p], A[q], A[r]):
            
            return 1
        
        else:
            
            p += 1
            q += 1
            r += 1
            
    return 0
