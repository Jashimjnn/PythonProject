thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#print
#print(thisdict)

#item access
#print(thisdict["brand"])

#length
#print(len(thisdict))

#type
#print(type(thisdict))

#It is also possible to use the dict() constructor to make a dictionary.
# thisdict1 = dict(name = "John", age = 36, country = "Norway")
# print(thisdict1)

#Access element
# x = thisdict.get("model")
# print(x)
# y = thisdict.keys()
# print(y)
# z = thisdict.values()
# print(z)
# p = thisdict.items()
# print(p)

#Updating
# thisdict.update({"year": 2020})
# print(thisdict)

#Adding Items
# thisdict["Age"] = 25
# print(thisdict)

#Popping item
# thisdict.pop("model")
# print(thisdict)
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
# thisdict.popitem()
# print(thisdict)
# del thisdict["model"]
# print(thisdict)
#The del keyword can also delete the dictionary completely:
# del thisdict
# print(thisdict)
#The clear() method empties the dictionary
# thisdict.clear()
# print(thisdict)

#Loop Through a Dictionary
#Print all key names in the dictionary, one by one:
# for x in thisdict:
#   print(x)
#Print all values in the dictionary, one by one:
# for x in thisdict:
#   print(thisdict[x])
#You can also use the values() method to return values of a dictionary:
# for x in thisdict.values():
#   print(x)
#You can use the keys() method to return the keys of a dictionary:
# for x in thisdict.keys():
#   print(x)
#Loop through both keys and values, by using the items() method:
# for x, y in thisdict.items():
#   print(x, y)


#Copy a Dictionary
# mydict = thisdict.copy()
# print(mydict)
# mydict = dict(thisdict)
# print(mydict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print(myfamily)
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])