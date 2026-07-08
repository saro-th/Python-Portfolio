"""
Script to calculate the sum of all natural numbers from 1 up to a user-inputted integer.
"""

def add_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = add_up_to(n)
    print(result)