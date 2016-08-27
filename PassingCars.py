# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    east = 0    # total cars travelling east
    west = 0    # 1 if car is travelling west, 0 otherwise
    passingCars = 0 # total passing cars
    
    totalCars = len(A)
    
    for i in range(totalCars):
        
        direction = A[i]
        
        # if car is heading in east direction then we increment east
        if direction == 0:
            
            east += 1
        
        # else the car is heading in west direction so we increment west
        else:
            
            west = 1
            
            # passing cars are the number of cars going east 
            # times the number of cars going west
            passingCars += east 
            
            # if the current car is going west and the next car is going east
            # then we reset west to 0 since a car going east followed by a car
            # going west will never pass each other
            if i != totalCars-1 and A[i+1] == 0:
                
                west = 0 
        
        if passingCars > 1000000000:
            
            return -1
            
    return passingCars

