"""
creator - debri

(completed)

Write a function that returns a string in which firstname is swapped with last name.
"""


def name_shuffler(str_):
    return str_[str_.index(' ') + 1:] + ' ' + str_[:str_.index(' ')]
