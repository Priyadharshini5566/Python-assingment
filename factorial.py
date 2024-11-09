
def factorial_iterative(n):
    """
    Calculate factorial using iteration.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def main():
    
    num = int(input("Enter a positive integer: "))

    
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        
        iterative_result = factorial_iterative(num)
        recursive_result = factorial_recursive(num)

        
        print(f"Iterative Factorial: {num}! = {iterative_result}")
        print(f"Recursive Factorial: {num}! = {recursive_result}")

if __name__ == "__main__":
    main()
