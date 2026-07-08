"""
Script to calculate the square of a user-inputted integer.
"""

def square(b):
    return b * b

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    result = square(n)
    print(result)