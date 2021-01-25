"""
creator - hakt


(completed)


The function must return the truncated version of the given string up to the given limit followed or concatenated by "..." if the result is shorter than the original. Return the same string if nothing was truncated.

Example:

solution('Testing String', 3) --> 'Tes...'
solution('Testing String', 8) --> 'Testing ...'
solution('Test', 8)           --> 'Test'
"""

### completed in 1 line

def solution(string, limit):
    return string if len(string) <= limit else string[:limit] + '...'
    
