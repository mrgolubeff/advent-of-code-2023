'''
Initial puzzle
'''

digits = [str(x) for x in range(10)]
numbers = []

with open('day1-puzzle1-input.txt') as f:
    for line in f:
        current_digit = ""
        first_digit = ""
        last_digit = ""
        counter = 0
        for symbol in line:
            if symbol in digits and counter == 0:
                first_digit = symbol
                current_digit = symbol
                counter += 1
            elif symbol in digits:
                current_digit = symbol
                counter += 1
        last_digit = current_digit
        numbers.append(int(first_digit + last_digit))

print(
    sum(numbers)
)
