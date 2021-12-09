 #If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. \
 #file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Calculate storage function

# Input: 4097
# Output: 8192

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize //block_size

    #Use the modulo operator to check whether there's any remainder:
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return block_size(full_blocks+1)
    return block_size*full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192