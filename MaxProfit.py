# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    max_profit = 0
    
    if len(A) > 1:
        
        buy_price = A[0]
        
        for i in range(1, len(A)):
            
            sell_price = A[i]
            
            if sell_price - buy_price > 0:
                
                if sell_price - buy_price > max_profit:
                    
                    max_profit = sell_price - buy_price
                
            else:
                
                buy_price = A[i]
    
    return max_profit
