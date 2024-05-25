binary_number = input("Enter a binary number: ")

if not binary_number.isdigit():
    print("Invalid binary number")
    exit()

decimal_number = 0
for digit in binary_number:
    decimal_number *= 2
    decimal_number += int(digit)

print("The decimal equivalent of", binary_number, "is", decimal_number)
