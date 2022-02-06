dictionary={
    "name":"Abhishek",
    "name1":"Aryan",
    "name2":"Bhavya",
    "name3":"Candy",
    "name4":"Dasie",
    "name5":"Himank",
    "other":{"name1":"Zara"}
}
#printing dictionay elements 
print(dictionary)

#printing using .items property
print(dictionary.items())

#printing key values only
print(dictionary.keys())

#updating existing key value
dictionary.update({"name6":"Kanika"})
print(dictionary)

print(dictionary["name5"])

#printing a particular using .get method
print(dictionary.get("name5"))
