def decimal_to_binary(decimal_number):
    if not (0 <= decimal_number <= 255):
        print("Input must be between 0 and 255.")
    
    binary_str = ""
    
    for i in range(7, -1, -1):
        if decimal_number & (1 << i):
            binary_str += "1"
        else:
            binary_str += "0"
    
    return binary_str

print(decimal_to_binary(102)) 