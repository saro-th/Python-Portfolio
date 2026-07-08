"""
Script to compare two user-inputted integers and return the maximum value.
"""

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = find_max(a, b)
    print(result)