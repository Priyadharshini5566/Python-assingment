
def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms.

    Returns:
        list: Fibonacci sequence.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main():
    
    n = int(input("Enter number of terms: "))

    
    fib_seq = fibonacci(n)
    print("Fibonacci Sequence:", ", ".join(map(str, fib_seq)))

if __name__ == "__main__":
    main()
