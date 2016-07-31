# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(K, A):
   
   answer = 0 
   
   totalLength = 0   
   
   for i in range(len(A)):
       
       ropeLength = A[i]
       
       if ropeLength >= K:
           
           answer += 1
           totalLength = 0
           
       else:
            
            totalLength += ropeLength
            
       if totalLength >= K:
            
            answer += 1
            totalLength = 0
            
   return answer
