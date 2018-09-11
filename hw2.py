


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

https://www.researchgate.net/post/What_is_differance_between_String_and_token_
in_Natural_Language_Processing_techniques

A simplified definition of a token in NLP is as follows: A token is a string
of contiguous characters between two spaces, or between a space and
punctuation marks. A token can also be an integer, real, or a number with a
colon (time, for example: 2:00). All other symbols are tokens themselves
xcept apostrophes and quotation marks in a word (with no space), which in many
cases symbolize acronyms or citations. A token can present a single word or a
group of words (in morphologically rich languages such as Hebrew) as the
following token "ולאחי" (VeLeAhi) that includes 4 words "And to my brother".

"""
import re
from collections import Counter

# # TODO Get text information from Harrison
# with open('11532192.txt', 'r') as fin:
#     my_text = fin.read()
#
# # re to remove special chars and punctuation
# my_text = re.sub(r'[^\w]', ' ', my_text)
#
# token_count = len(my_text.split())
# print('Token count:\n', token_count)
#
# text_histogram = Counter(my_text.split())
# print('\nType/text histogram:\n', text_histogram)
#
# type_count = len(text_histogram)
# print('\nType count:\n', type_count)

### Attempt two

with open('11532192.txt', 'r') as fin:
    my_text = fin.read()

new_text = re.sub('\n', '.', my_text)
new_text = my_text.split()

cleaned_text_list = []

# TODO lowercase conflicts

count_incomplete = 0
count_complete = 0

for i in new_text:
    count_complete += 1


    # if it's *only* a special char, don't keep it.

    # if it's a float, keep it as is. remove trailing '.'
    if re.search('\.', i):
        try:
            float(i)
            i = i.strip('\.')
            cleaned_text_list.append(i.lower())
            continue

        except:
            pass

    if re.match(r'^\w+$', i):
        cleaned_text_list.append(i.lower())
        continue


    # after handling numbers, it's safe to clean a bit more

    for j in [':', '\.', '\)', '\(', ',', ';', '\]', '\[']:

        i = re.sub(j, '', i)

    i = i.strip('"')
    i = i.strip("'")
    i = i.strip()

    if len(i) == 0:
        cleaned_text_list.append(i.lower())
        continue

    if len(i) == 1:
        cleaned_text_list.append(i.lower())
        continue

    # These are the most odd looking tokens
    # print(i)
    cleaned_text_list.append(i.lower())
    count_incomplete += 1

print(count_complete)
print("Odd looking tokens (weird chars, outliers):", count_incomplete)

print("Token total:", len(cleaned_text_list))
# print(cleaned_text_list)

c = Counter(cleaned_text_list)
# print(c)
print("Type total:", len(c))
