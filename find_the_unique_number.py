"""
creator - isqua


(completed)


There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


### no built-in functions used!
### after a few minutes I realized I could use a bubble
### sorting algorithm but I felt that wouldn't challenge
### me enough so I found out a way to brute force the answer.


def find_uniq(arr):

    for number in arr:

        if arr[-1] == arr[-2]:
            if number != arr[-1]:
                return number

        if arr[-1] != arr[-2]:
            if number == arr[-1]:
                return arr[-2]
            elif number == arr[-2]:
                return arr[-1]
