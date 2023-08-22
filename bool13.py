def main(b):
    """
    Check if the given number is divisible by only one of 3 or 5.
    Args:
        b: int
    Returns:
        bool
    """
    # Write your code here
    return (b%3==0 or b%5==0) and b%15!=0
