import os 
"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""
dictionary = {
    'one': '1', 
    'two': '2',
    'three': '3',
    'four': '4',
    'five' : '5', 
    'six': '6',
    'seven' : '7', 
    'eight': '8',
    'nine': '9' 
}

with open('example.txt', 'r') as file:
    line = file.readline()
    counter = 1
    result = 0 
    while line:
        first_digit = None
        last_digit = 0
        word = ""
        for char in line:
            if char.isdigit():
                last_digit = char
                print(f"{counter} found - {char}")
                if first_digit is None:
                    first_digit = char

                word = ""
            else:
                word += char
                number = dictionary.get(word)
                if number != None:
                    last_digit = number
                    print(f"{counter} found - {number}")
                    if first_digit is None:
                        first_digit = number
                    
                    word = word[-1]

                elif not any(key.startswith(word) for key in dictionary):
                    word= word[1:]
                    
                
        print(f"    {counter} line is {first_digit}{last_digit}")
        result += int(first_digit+last_digit)

        line = file.readline()
        counter += 1
    print(f"The result for part 2 is {result}")