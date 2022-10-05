fruits =  ['apples','mangoes','oranges','grapes']

data =  {'name':'Alex','age':16, 'isTall':True}

# loop over all the elements in the given fruits list and print name and index of each item

for fruit in fruits:
    print(fruit)
    print(fruits.index(fruit))


# loop over all elements in data dict and print key : value for each key, value [air]


for key,value in data.items():
    print(key, " : ", value)