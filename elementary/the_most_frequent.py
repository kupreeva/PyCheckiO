"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
Input: a list of strings.
Output: a string.
"""

def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    dict_of_strings = {}
    for item in data:
        if item not in dict_of_strings:
            dict_of_strings[item] = 1
        else:
            dict_of_strings[item] = dict_of_strings[item] + 1
    max_value = max(dict_of_strings.values())
    for key in dict_of_strings:
        if dict_of_strings[key] == max_value:
            return key

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
