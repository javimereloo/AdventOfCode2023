import os 
"""
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map;
on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") 
and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where
do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, 
we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by 
a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading 
the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value 
that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last 
digit (in that order) to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""

with open('input.txt', 'r') as file:
    line = file.readline()

    result = 0 
    while line:
        first_digit = None
        last_digit = 0
        for char in line:
            if char.isdigit():
                last_digit = char
                if first_digit is None:
                    first_digit = char
                

        result += int(first_digit +last_digit)

        line = file.readline()

    print(f"The result for part 1 is  {result}")


