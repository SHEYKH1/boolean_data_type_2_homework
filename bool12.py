def main(a):
    """
    Check if a given number is divisible by either 3 or 5.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a%3==0 or a%5==0
print(main(0))
