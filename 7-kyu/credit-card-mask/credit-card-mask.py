# return masked string
def maskify(cc):
   #split the string into a list?
    split_info = list(cc)
    print(split_info)
    #iterate through the list and hash everything, except the final 4 items
    hashed_list = ['#'] * (len(split_info) - 4) + split_info[-4:]
    hashed_string = ''.join(hashed_list)
    return hashed_string
                
​