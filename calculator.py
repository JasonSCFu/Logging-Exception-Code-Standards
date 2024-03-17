"""
This is a module-level docstring.

It provides an overview of the purpose and contents of the module.
"""
def add(a, b):
    """
    Adds two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    result = a + b
    return result

def main():
    """
    Main function to demonstrate the use of the add function.
    """
    x = 5
    y = 3
    z = add(x, y)
    print(z)

if __name__ == "__main__":
    main()
