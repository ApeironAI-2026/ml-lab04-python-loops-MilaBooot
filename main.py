def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Example: 5! = 120
    """
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    
    # Initialize result to 1
    result = 1
    
    # Loop from 1 to n (inclusive)
    # Handle the special case of n=0 (loop won't execute, result stays 1)
    for i in range(1, n + 1):
        result = result * i
    
    # Return the calculated factorial
    return result