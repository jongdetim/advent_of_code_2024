def is_safe_row(row):
    """Check if a row is safe."""
    return (all(1 <= row[i] - row[i-1] <= 3 for i in range(1, len(row))) or
            all(1 <= row[i-1] - row[i] <= 3 for i in range(1, len(row))))

def can_be_safe_by_removing_one(row):
    """Check if a row can be made safe by removing one item."""
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if is_safe_row(new_row):
            return True
    return False

def process_data(data):
    """Process the data to count safe and unsafe rows."""
    safe, unsafe = 0, 0
    for row in data:
        row = [int(num) for num in row if num.isdigit()]
        if is_safe_row(row) or can_be_safe_by_removing_one(row):
            safe += 1
        else:
            unsafe += 1
    return safe, unsafe

with open("input") as file:
    data = [line.split() for line in file]

safe, unsafe = process_data(data)
print(f"Safe: {safe}, Unsafe: {unsafe}")
