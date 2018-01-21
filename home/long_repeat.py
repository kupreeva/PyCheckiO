"""
Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" 
contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes
it an answer.
Input: String.
Output: Int.
"""

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    longest = 0
    lstr = 0
    for i in range(len(line)):
        if i>0:
            if line[i] != line[i-1]:
                lstr = 0
        lstr += 1
        if lstr > longest:
            longest = lstr
    return longest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
