""" 
Calculator with basic operations.
Demonstrates unit testing and CI/CD automation
"""

def add(a, b):
    """Retrun a plus b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a multiplied by b."""
    return a * b


def divide(a, b):
    """Return a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

# Example usage
if __name__ == "__main__":
    print("Calculator Demo")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"2 ^ 3 = {power(2, 3)}")

