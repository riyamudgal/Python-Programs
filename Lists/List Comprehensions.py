#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#creating new list from exisitng having a constraint that 'a' must be there
fruits = ["apple","grapes", "banana","watermelon", "cherry", "kiwi"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#coverting fruits list to upper case
newlist = [x.upper() for x in fruits]
print(newlist)

#printing each character of string in list
List = [character for character in 'Spread Kindness']
print(List)

#output
['S','p','r','e','a','d',' ','K','i','n','d','n','e','s','s']



#printing positive numbers
list1 = [-10,32,-21,65,-4,-76,45,-66,12,93]
pos_nums= [num for num in list1 if num >= 0]
print("Positive numbers in the list: ", pos_nums)

