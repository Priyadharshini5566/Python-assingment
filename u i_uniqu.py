
def has_unique_chars(s):
    """
    Check if a string has all unique characters.

    Args:
        s (str): Input string.

    Returns:
        bool: True if all characters are unique, False otherwise.
    """
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Use set to check for uniqueness
    return len(s) == len(set(s))

def main():
    # Take string input
    s = input("Enter a string: ")
    
    # Check for unique characters
    result = has_unique_chars(s)
    
    # Print result
    print(f"Has unique characters: {result}")

if __name__ == "__main__":
    main()
