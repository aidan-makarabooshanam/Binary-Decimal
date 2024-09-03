def binarytodecimal(binary_string):

    decimal_value = 0
    
    for i in range(len(binary_string)):
        bit = int(binary_string[i])
        
        power = len(binary_string) - 1 - i
        
        decimal_value += bit * (2 ** power)
    
    return decimal_value
print(binarytodecimal("00001010"))