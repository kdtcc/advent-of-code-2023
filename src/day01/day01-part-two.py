def find_calibration_value(str):
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }
    
    first_occ_to_index = {digit: str.find(digit) for digit in digits if str.find(digit) >= 0}
    last_occ_to_index = {digit: str.rfind(digit) for digit in digits if str.rfind(digit) >= 0}

    first_occurrence_idx = min(first_occ_to_index.values())
    last_occurrence_idx = max(last_occ_to_index.values())

    first_char_digit = '0'
    last_char_digit = '0'

    # Find first digit
    for k, v in first_occ_to_index.items():
        if v == first_occurrence_idx:
            first_char_digit = digits[k]
            break

    # Find last digit
    for k, v in last_occ_to_index.items():
        if v == last_occurrence_idx:
            last_char_digit = digits[k]
            break

    return int(first_char_digit + last_char_digit)

def main():
    file = open("./day01/input.txt", "r")

    # sum will contain the sum of the calibration values
    sum = 0

    for line in file:
        # Get the correct calibration value before adding it to the sum
        calibVal = find_calibration_value(line)
        sum += calibVal

    print (sum)

main()