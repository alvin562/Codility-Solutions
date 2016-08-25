# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


import sys


# swaps elements in positions i and j
def swap(A, i, j):
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# used for quicksort
def partition(A, lo, hi):
    
    pivot = A[hi]  # our pivot is always the last element of array
    wall = lo   # we will swap the pivot with this index
    
    # we walk through the array
    # if we find an element less than or equal to
    # the pivot then we swap it with the element at wall
    # and move the wall up one position
    for i in range(lo, hi):
        
        if abs(A[i]) <= abs(pivot):
            
            swap(A, wall, i)
            wall += 1
            
    swap(A, wall, hi)
    return wall
    

def quickSort(A, lo, hi):
    
    if lo < hi:
        
        pivot = partition(A, lo, hi)
        quickSort(A, lo, pivot-1)
        quickSort(A, pivot+1, hi)
    

# findMinAbsSum finds the min abs sum by 
# first sorting the values in A by absolute value
# then walks through the way in a caterpillar-like fashion
# to calculate the min abs sum
def findMinAbsSum(A):
    
    quickSort(A, 0, len(A)-1)
    minAbsSum = sys.maxint
    
    i = 0
    j = 0
    
    sz = len(A)-1
    
    while i <= sz and j <= sz:
        
        if abs(A[i] + A[j]) < minAbsSum:
            
            minAbsSum = abs(A[i] + A[j])
            
        # we can break if the minAbsSum ever reaches 0 since
        # there cannot possibly be any smaller sum
        if minAbsSum == 0:
            
            break
        
        # caterpillar walk
        if i == j:
            
            j += 1
        
        else:
            
            i += 1
            
    return minAbsSum


def solution(A):
    # write your code in Python 2.7
    
  #  B = [-1, 2, 5, -3, -100, 6, 7, 2, 2, 1, 9, -200, 201]
    
    answer = findMinAbsSum(A)
    
 #   for i in range(len(A)):
        
#        print(A[i])
        
    return answer
