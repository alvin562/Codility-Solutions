# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    
    stack = []
    
    for i in range(len(S)):
        
        if S[i] == '(':
            
            stack.append(S[i])
        
        else:
            
            if len(stack) > 0:
                nest = stack.pop() + S[i]
            
            
                if nest != '()':
                
                    return 0
                    
            else:
                
                return 0
        
    if len(stack) > 0: 
        
        return 0
        
    return 1
