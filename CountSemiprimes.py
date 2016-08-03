# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math


# this solution still needs a lot of fixing
# it only gets a 55% on codility since the performance
# is really bad (runs in O(N*log(log(N)) + M*N when
# it is supposed to run in O(N*log(log(N)) + M)


# returns a list of primes under a given limit
# using the Sieve of Eratosthenes algorithm
def generatePrimes(n):
    
    primes = []
    
    # initialize list of boolean values initially set all to True
    a = [True for i in range(n)]
    sqrtN = int(math.sqrt(n))
    
    for i in range(2, sqrtN):
        
        if a[i]:
            
            k = 0
            j = i**2 + i*k
            
            while j < n:
                
                a[j] = False
                k += 1
                j = i**2 + i*k
                
    for i in range(2, len(a)):
        
        # if a[i] is prime we add it to our list of primes
        if a[i]:    
            
            primes.append(i)
    
    return primes
    
  
# returns a list of semiprimes under a given value
def generateSemiprimes(n):
    
    semiprimes = []
    
    # list of boolean values where indices represent semiprime numbers
    # (i.e. True if index i is semiprimes and false otherwise)
    a = [False for i in range(n)] 
    primes = generatePrimes(n)
    
    for i in range(len(primes)):
        
        for j in range(len(primes)):
            
            if primes[i]*primes[j] <= n:
                
                semiprime = primes[i]*primes[j]
                a[semiprime-1] = True
            
            else:
                
                break
            
    for i in range(len(a)):
        
        # if a[i] is semiprime then we add it to our list of semiprimes
        if a[i]:
            
            semiprimes.append(i+1)
        
    return semiprimes


def solution(N, P, Q):
    # write your code in Python 2.7
    
    semiprimes = generateSemiprimes(N)
    answer = []
    
    for i in range(len(P)):
        
        total = 0
        
        for j in range(P[i], Q[i]+1):    # inclusive range
            
            if j in semiprimes:
            
                total += 1
        
        answer.append(total)
    
    return answer
