"""
creator - kenkamau


(incomplete)


Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down),
these numbers remain the same. To clarify, if we write them down on a paper and turn
the paper upside down, the numbers will be the same. Try it and see! Some numbers such
as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range.
For example, solve(0,10) = 3, because there are only 3 upside down 
numbers >= 0 and < 10. They are 0, 1, 8.
"""

def solve(a, b):


    for i in range(a, b):


        if int(str(i)[0]) in [0, 1, 6, 8, 9]:
            return i
