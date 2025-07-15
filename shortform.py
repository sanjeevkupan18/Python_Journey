def print_initials(full_name):
    # Split the full name into individual parts
    name_parts = full_name.split()
    
    # Extract the first letter of each part and convert it to uppercase
    initials = ''.join(part[0].upper() for part in name_parts)
    
    # Print the initials
    print(initials)

# Example usage
full_name = "mohan karam gandhi"
print_initials(full_name)
