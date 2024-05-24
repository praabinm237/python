# name="hello world"
# print(len(name))

# print(name.upper())
# print(name.strip())
# print(name.split()) # in default, separated by space otherwise we can define separator

#list
fruit=[
    'kiwi'
]
vegetables=[
    'spinach',
    'potato'
]
fruit.extend(vegetables)
fruit.append("apple")
fruit.append("banana")
fruit.insert(1,'mango')
fruit.remove('kiwi')
print(fruit)
fruit.pop(2)
print(vegetables.index('potato'))
print(fruit)