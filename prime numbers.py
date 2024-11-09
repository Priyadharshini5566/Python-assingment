
def find_primes(start, end):
    """
    Find all prime numbers in a given range.

    Args:
        start (int): Start of the range (inclusive).
        end (int): End of the range (inclusive).

    Returns:
        list: List of prime numbers in the range.
    """
    primes = []

    for num in range(start, end + 1):
        if num > 1:  
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

    return primes

def main():
    
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    
    if start > end:
        print("Error: Invalid range. Start should be less than or equal to end.")
    else:
        
        primes = find_primes(start, end)
        print(f"Prime numbers between {start} and {end}: {primes}")

if __name__ == "__main__":
    main()
