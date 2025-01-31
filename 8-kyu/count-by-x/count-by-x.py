def count_by(x, n):
    #init an array with the first number as the first value
    results = []
        
    for i in range(1, n + 1):
        results.append(x * i)
    
    return results  