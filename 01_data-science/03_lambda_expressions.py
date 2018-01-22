from __future__ import print_function

from functools import reduce


# Create a list
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Add bangs
fellow_bang = map(lambda member: member + '!!!', fellowship)
print(list(fellow_bang))

# Select names with more than 6 letters
fellow_len = filter(lambda member: len(member) > 6, fellowship)
print('\nMore than 6 letters: \n {} \n'.format(list(fellowship)))

# Reduce
fellow_reduce = reduce(lambda a, b: a + b + ' ', fellowship)
print('\nReducing: \n {} \n\n'.format(fellow_reduce))


