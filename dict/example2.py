# Loop through a dictionary 
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)

# # Loop through keys
# for x in thisdict.keys():
#   print(x)

# Copy a Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function
mydict2 = dict(thisdict)
print(mydict2)
