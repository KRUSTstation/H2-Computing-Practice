def decompress(compressed_list, byte_rep, bytes_pattern):
    pattern = []
    count = 0
    while count <= len(bytes_pattern) - 2:
        pattern.append(bytes_pattern[count:count+2])
        count+=2

    count = 0
    while count < len(compressed_list):
        byte = compressed_list[count]

        if byte == byte_rep:
            compressed_list.pop(count)
            
            for i in range(len(pattern)):
                compressed_list.insert(count+i, pattern[i])

        count += 1
    
    return compressed_list
	
	
	
#main program

#type your client code here
