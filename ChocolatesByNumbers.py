def gcd(a, b):
    
    while b != 0:
        
        t = b
        b = a % b
        a = t
        
    return a
    
def lcm(a, b):
    
    return a*b/gcd(a, b)


def solution(N, M):
    # write your code in Python 2.7

    return lcm(N, M)/M
