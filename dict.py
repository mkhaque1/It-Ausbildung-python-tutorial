# dictionary example and methods in python

thisdict = {
  "brand": "Ford", # key value pair
  "model": "Mustang",
  "year": 2021
}
# print(thisdict)
print(len(thisdict)) # accessing the number of key-value pairs
print(thisdict["year"]) # accessing value using key

dic2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(dic2["colors"]) # accessing the list of colors

# methods in dictionary
dic2.pop("electric") # removing a key-value pair
print(dic2)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# adding a new key-value pair
car.update({"color": "White"})

print(car)