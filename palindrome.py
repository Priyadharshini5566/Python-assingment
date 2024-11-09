
def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    
    s = s.replace(" ", "").lower()
    
    
    return s == s[::-1]


print(is_palindrome("Madam"))  # True
print(is_palindrome("Hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Not a palindrome"))  # False


