def hash_function(s):
    """
    Python implementation of the hash function from 
    The C Programming Language by Brian Kernighan and Dennis Ritchie.
    
    Args:
        s (str): The string to hash
        
    Returns:
        int: The hash value
    """
    hashval = 0
    for char in s:
        hashval = ord(char) + 31 * hashval
    return hashval % 101

# Test the hash function
if __name__ == "__main__":
    test_strings = [
        "hello",
        "world",
        "python",
        "hash",
        "function",
        "algorithm",
        "kernighan",
        "ritchie",
        "programming",
        "language"
    ]
    
    print("String\t\tHash Value")
    print("-" * 30)
    for s in test_strings:
        print(f"{s:<15}\t{hash_function(s)}")
    
    # Test for collisions
    all_values = {}
    for i in range(1000):
        test_str = f"test{i}"
        hash_val = hash_function(test_str)
        if hash_val in all_values:
            all_values[hash_val].append(test_str)
        else:
            all_values[hash_val] = [test_str]
    
    # Count collisions
    collisions = sum(len(strings) - 1 for strings in all_values.values() if len(strings) > 1)
    print(f"\nCollision test with 1000 strings:")
    print(f"Number of unique hash values: {len(all_values)}")
    print(f"Number of collisions: {collisions}")
    print(f"Collision rate: {collisions/1000:.2%}")
    
    # Explanation of the constants
    print("\nExplanation of constants:")
    print("31: Prime multiplier that helps in distributing hash values")
    print("101: Prime modulus that determines the range of hash values (0-100)") 