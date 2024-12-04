import re

with open("input") as file:
    data = file.read()

def find_and_sum_multiplications(text):
    """
    Finds all occurrences of mul(X,Y), where X and Y are 1-3 digit numbers,
    multiplies them, and returns the total sum. Spaces inside the parentheses
    or around the comma are not allowed.

    Args:
        text (str): The input string to search for mul(X,Y) patterns.

    Returns:
        int: The total sum of all valid multiplications.
    """
    # Regular expression to match strict mul(X,Y) pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches
    matches = re.finditer(pattern, text)
    
    # Calculate the total sum
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum


result = find_and_sum_multiplications(data)
print("Total Sum:", result)
