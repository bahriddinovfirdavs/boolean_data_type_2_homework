def main(a):
    """
    Given integer is less of 10000 . Check if the sum of digits is odd .
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here 9876
    return a<10000 and ((a%10)+(a//10%10)+(a//100%10)+(a//1000))%2==1 and ((a%10)+(a//10%10)+(a//100%10)+(a//1000))%2!=0 and a>0 
print(main(int(input())))
    