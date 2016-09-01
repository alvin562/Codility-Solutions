# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def swap(i, j, A):
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(l, r, A):
    
    pivot = A[r]
    wall = l
    
    for i in range(l, r):
        
        if A[i] < pivot:
            
            swap(i, wall, A)
            wall += 1
            
    swap(wall, r, A)
    
    return wall
    
    
    
def quick_sort(l, r, A):
    
    if l < r:
        
        pivot = partition(l, r, A)
        quick_sort(l, pivot-1, A)
        quick_sort(pivot+1, r, A)


def print_elements(A):
    
    for i in range(len(A)):
        
        print(A[i])


def solution(A):
    # write your code in Python 2.7
    
    # quick_sort(0, len(A)-1, A)
    
    A.sort() # built in sort function is faster (also note that we could use bookkeeping to run in O(n))
    
    P1 = A[len(A)-1]
    Q1 = A[len(A)-2]
    R1 = A[len(A)-3]
    
    P2 = A[0]
    Q2 = A[1]
    R2 = A[len(A)-1]
    
    return max(P1*Q1*R1, P2*Q2*R2)
