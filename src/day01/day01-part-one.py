file = open("input.txt", "r")

sum = 0

for line in file:
    digits = [c for c in line if c.isdigit()]
    calibVal = int(digits[0] + digits[-1])
    sum += calibVal
print (sum)