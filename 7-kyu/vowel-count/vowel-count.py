def get_count(sentence):
    #use a counter for the amount of vowels
    vowel_count = 0
    #define vowels
    vowels = "aeiou" #but not y ;) 
    #iterate through the sentance given 
    for char in sentence:
        #check if char in stentence is a vowel
        if char in vowels:
            #increment the count
            vowel_count += 1
            
    #return the total number of vowels based on the count
    return vowel_count