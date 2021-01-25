"""
creator - Deantwo


(completed)


In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


### this one was quite satisfying. 
### I managed to shrink it from about
### 8 lines to essentially just 1
### tacky yet fun line

def high_and_low(numbers):
    return f'{sorted([int(i) for i in numbers.split()])[-1]} {sorted([int(i) for i in numbers.split()])[0]}'
