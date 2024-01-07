def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def sum_of_hashes(initialization_sequence):
    steps = initialization_sequence.split(',')
    total_sum = 0
    for step in steps:
        key, value = step.split('=')
        result = hash_algorithm(value)
        total_sum += result
    return total_sum

# Example usage:
initialization_sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
result_sum = sum_of_hashes(initialization_sequence)
print(result_sum)
