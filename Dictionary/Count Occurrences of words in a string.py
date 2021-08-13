def word_count(str):
    counts = dict()                  #Dictionary can also be created by the built-in function dict()
    words = str.split()              #split(), Split a string into a list where each word is a list item

    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts
string=input("Enter the string ")
print( word_count(string))

'''
Output
Enter the string split(), Split a string into a list where each word is a list item
{'split(),': 1, 'Split': 1, 'a': 3, 'string': 1, 'into': 1, 'list': 2, 'where': 1, 'each': 1, 'word': 1, 'is': 1, 'item': 1}
'''
