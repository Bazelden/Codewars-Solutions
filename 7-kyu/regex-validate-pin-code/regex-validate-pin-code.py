def validate_pin(pin):
    # check the length of the pin to ensure it's valid
    if len(pin) == 4 or len(pin) == 6:
        #check to see if passed argument is all digits
        if pin.isnumeric():
            return True
    return False

#AI gen 1 liner
#def validate_pin(pin):
    #return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()
