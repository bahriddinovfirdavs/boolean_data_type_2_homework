def main(a):
    """
    Check if a given year is a leap year. Leap year is  is divisible by 4 and 400 but not by 100.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return (a%100!=0 and a%4==0) or (a%400==0)
