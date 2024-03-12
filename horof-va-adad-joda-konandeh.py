def separate_chars_and_digits(input_string):
    chars = []
    digits = []
    for char in input_string:
        if char.isalpha():
            chars.append(char)
        elif char.isdigit():
            digits.append(char)
    return chars, digits

input_string = input("Please enter the desired string: ")
separated_chars, separated_digits = separate_chars_and_digits(input_string)

print("Letters: ", "".join(separated_chars))
print("Digits: ", "".join(separated_digits))