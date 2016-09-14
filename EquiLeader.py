# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def get_leader(A):
    
    leader = A[0]
    total = 1
    
    for i in range(1, len(A)):
        
        if leader != A[i]:
            
            if total == 0:
                
                leader = A[i]
                
            else:
                
                total -= 1
                
        else:
            
            total += 1
            
    return leader



def solution(A):
    # write your code in Python 2.7
    
    equi_leaders = 0
    
    if len(A) > 1:
    
        global_leader = get_leader(A)
        total_leaders = A.count(global_leader)
    
        lhs_leaders = 0   # number of leaders on lhs
        equi_leaders = 0
    
        for i in range(len(A)-1):
        
            lhs = i+1   # total elements on lhs
            rhs = len(A) - lhs  # total elements on rhs
        
            if A[i] == global_leader:
            
                lhs_leaders += 1
            
            if lhs_leaders > lhs/2 and total_leaders-lhs_leaders > rhs/2:
                
                equi_leaders += 1
        
    return equi_leaders
        
