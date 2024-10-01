'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
def is_factorial_number(n):
    """Check if n is a factorial number."""
    if n < 0:  # Factorials are non-negative integers
        return False
    
    i = 1
    factorial = 1
    
    # Calculate factorial iteratively until it exceeds n
    while factorial < n:
        i += 1
        factorial *= i
    
    # Check if the calculated factorial equals n
    return factorial == n

def main():
    """Main function to check if the input number is a factorial number."""
    try:
        n = int(input("Enter a number: "))  # Prompt for clarity
        
        # Check if n is a factorial number
        if is_factorial_number(n):
            print("Yes")
        else:
            print("No")
    except ValueError:
        print("Please enter a valid 
