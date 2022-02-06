mydict={
    "name":"sakssham mudgal",
    "class": "btech",
    "roll no":[1900330100188,2019]
}

#can use single quotes
print(mydict['name'])
print(mydict['class'])
print(mydict['roll no'])

#can use double quotes
print(mydict["name"])
print(mydict["class"])
print(mydict["roll no"])

#nested dictionary
myfirstdict={
    "name":"Kelvin Peterson",
    "class": "MBA",
    "roll no":[1900330100188,2019],
    "subjects": {                                                 #nested dictionay element can have only one key:value
                "first":"OS",
                }
}

print(myfirstdict["name"])
print(myfirstdict["class"])
print(myfirstdict["subjects"])
print(myfirstdict["subjects"]['first'])

#dictionay is mutable i.e., changeable
myfirstdict["class"]="MCA"
print(myfirstdict)


