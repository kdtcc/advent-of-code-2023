import re

def contains_symbol(border):
    # Returns true if the border contains a symbol (something different from a dot or a digit)
    for c in border:
        if c != '.' and not c.isdigit():
            return True
        
    return False

def main():
    part_sum = 0
    data = []
    with open("./src/day03/input.txt") as file:
        data = file.readlines()
    
    # Calculating the width of the array (each line has the same length)
    width = len(data[0])

    # For convenience, we insert a first line and last line full of dots
    dot_line = "." * (width - 1)
    data.insert(0, dot_line)
    data.append(dot_line)

    # We also add a first column and last columns of dots and remove the line break
    for i in range(0, len(data)):
        data[i] = data[i].strip()
        data[i] = "." + data[i]
        data[i] = data[i] + "."
    
    for i in range(0, len(data)):
        results = re.finditer(r'\d+', data[i])
        for res in results:
            border_start = res.start() - 1
            border_end = res.end() + 1

            # We create a string containing all the characters constituting the "border" of the number
            border = data[i-1][border_start:border_end] + data[i][border_start] + data[i][border_end - 1] + data[i+1][border_start:border_end]

            if contains_symbol(border):
                part_sum += int(res.group())
    
    print("The sum of the parts is ", part_sum)

main()