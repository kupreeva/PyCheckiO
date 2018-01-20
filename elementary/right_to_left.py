"""
You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are separated
by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even
if it's a part of another word. All strings are given in lowercase.
Input: A sequence of strings as a tuple of strings (unicode).
Output: The text as a string.
Precondition:
0 < len(phrases) < 42
"""

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    
    stroka = ''
    for item in phrases:
        if 'right' in item:
            item = item.replace('right','left')
        stroka = stroka + item +','
    stroka = stroka[0:len(stroka)-1]    
    # print(stroka)  
    return stroka

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
