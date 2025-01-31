def count_by(x, n):
    #init a list
    results = []
    
    # Loop through integers from 1 to n (inclusive)   
    for i in range(1, n + 1):
        # Multiply x by the current integer i and append the result to the list
        results.append(x * i)
    #return the list    
    return results  
