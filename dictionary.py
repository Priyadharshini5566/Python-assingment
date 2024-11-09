
def sort_dictionary(dictionary):
    """
    Sorts a dictionary by keys in ascending order.

    Args:
        dictionary (dict): Input dictionary.

    Returns:
        dict: Sorted dictionary.
    """
    return dict(sorted(dictionary.items()))

def main():
    
    num_items = int(input("Enter number of items: "))

    dictionary = {}
    for i in range(num_items):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value for {key}: ")
        dictionary[key] = value

    
    sorted_dict = sort_dictionary(dictionary)
    print("Sorted Dictionary:")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
