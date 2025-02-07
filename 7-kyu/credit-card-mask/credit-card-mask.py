# return masked string
def maskify(cc):
   #split the string into a list?
    split_info = list(cc)
    print(split_info)
    #determine length of list and subtract 4 from the length - replace additional characters with #
    hashed_list = ['#'] * (len(split_info) - 4) + split_info[-4:]
    #revert list back to string
    hashed_string = ''.join(hashed_list)
    #return :) 
    return hashed_string
                
​
