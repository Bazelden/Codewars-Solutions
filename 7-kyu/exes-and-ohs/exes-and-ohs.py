def xo(s):
    #create counters
    x_amount = 0
    o_amount = 0
    
    #iterate through the given string to check for an x or o and increase counter
    for char in s.lower():  # Convert to lowercase for case-insensitivity
        if char == 'x':
            x_amount += 1
        elif char == 'o':
            o_amount += 1
    
    #check to see if amount of x and o are the same or non-existent and return true, else return false.
    return x_amount == o_amount

    #The AI one liner ¬_¬
    #def xo(s):
    #return s.lower().count('x') == s.lower().count('o')
    
    
        
    
