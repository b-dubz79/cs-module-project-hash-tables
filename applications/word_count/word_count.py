import string
import re

def word_count(s):
    # Your code here
    word_dict = {}
    print('!!!', word_dict)
    
    if s == '':
        return word_dict
    # set string to lowerCase and split words into an array
    strings = s.lower()
    strings = strings.split()
    
    # remove puncuation with regex
    for i, word in enumerate(strings):
        print('ENUMERATE', strings)
        strings[i] = re.sub("[^a-z']+", '', word)
    
    for j in strings:
        if j not in word_dict:
            if j != '':
                word_dict[j] = 1
        else:
            word_dict[j] += 1
    print('@@@@', word_dict)
    return word_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

# # example_string = "The quick brown fox jumps over the lazy dog"

#     # remove spaced and throw it all in a lis
#     # print(string_list)t
# string_list = example_string.split()
# giant_string = "".join(string_list)

# letter_counts = {}

#     # iterate over string
# for letter in giant_string:
#     letter = letter.lower()
#     # check if letter in dict
#     if letter in letter_counts:
#         #if it is, increment count
#         letter_counts[letter] += 1
    
    
#     # if not add
#     else:
#         letter_counts[letter] = 1

#     # Print each letter, starting with the most common
#     # sort based on key's count
#   sorted_letter_counts = sorted(letter_counts.items(), key=lambda pair: pair[1], reverse = True)
#     for pair in sorted_letter_counts:
#         print(pair[0])