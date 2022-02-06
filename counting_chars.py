def char_count(str1):
    dict={}
    for i in str1:
        key = dict.keys()
        if i in key:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
    
string=input(" Enter the string ")
print(char_count(string))
