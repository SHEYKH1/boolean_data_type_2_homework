def main(a):
    """
    Check if a given number is negative or odd.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a%2!=0 or a<0
print(main(11))