def char_count(str1):
    dict={}
    for i in str1:
        key = dict.keys()
        if i in key:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
    
string=input(" Enter the string")
print(char_count(string))


#will count characters as well as blank spaces

'''
Output
#1st
Enter the string communication
{'c': 2, 'o': 2, 'm': 2, 'u': 1, 'n': 2, 'i': 2, 'a': 1, 't': 1}

#2nd
Enter the string Hey Start leaning, start now
{'H': 1, 'e': 2, 'y': 1, ' ': 4, 'S': 1, 't': 4, 'a': 3, 'r': 2, 'l': 1, 'n': 3, 'i': 1, 'g': 1, ',': 1, 's': 1, 'o': 1, 'w': 1}
'''
