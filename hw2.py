


"""

## Original Directions

Homework: type/token ratios

1. Write a program to count the number of word tokens in a text file.
Compare your output to a classmate’s. What decisions did you make
differently regarding what counts as “a" token?
2. Write a program to count the number of word types in a text file.
Compare your output to a classmate’s. What decisions did you make
differently regarding what counts as a type?
3. As you have seen, type/token ratios are widely used in research in
neurology, psychiatry, the social sciences, and the humanities. How
could a researcher’s definitions of “type" and “token" affect whether
or not they have a positive result to report?

"""
import re
from collections import Counter

# TODO Get text information from Harrison
with open('text.txt', 'r') as fin:
    my_text = fin.read()

# re to remove special chars and punctuation
my_text = re.sub(r'[^\w]', ' ', my_text)

token_count = len(my_text.split())
print('Token count:\n', token_count)

text_histogram = Counter(my_text.split())
print('\nType/text histogram:\n', text_histogram)

type_count = len(text_histogram)
print('\nType count:\n', type_count)





