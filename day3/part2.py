import re

with open("input") as file:
    data = file.read()

def find_and_sum_multiplications_with_instructions(text):
    """
    Processes a string with `do()` and `don't()` instructions that enable or disable
    `mul(X,Y)` operations. Only the enabled multiplications are summed.

    Args:
        text (str): The input string containing instructions and `mul` operations.

    Returns:
        int: The total sum of results from enabled `mul` operations.
    """
    # Regular expressions for instructions and strict mul patterns
    enable_pattern = r"do\(\)"
    disable_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Initialize variables
    enabled = True  # Initially, mul instructions are enabled
    total_sum = 0

    # Iterate through matches in the order they appear
    for match in re.finditer(f"{enable_pattern}|{disable_pattern}|{mul_pattern}", text):
        match_text = match.group()

        # Check if it's an enabling/disabling instruction
        if re.fullmatch(enable_pattern, match_text):
            enabled = True
        elif re.fullmatch(disable_pattern, match_text):
            enabled = False
        # Check if it's a valid mul(X,Y) operation
        elif enabled and (mul_match := re.fullmatch(mul_pattern, match_text)):
            x, y = map(int, mul_match.groups())
            total_sum += x * y

    return total_sum

result = find_and_sum_multiplications_with_instructions(data)
print("Total Sum:", result)
