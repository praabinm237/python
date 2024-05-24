people={
    'name':'Ram',
    'age':20,
    'gender':'male'
}
people.update({
    'name':'Ram Shrestha',
    'age':30

})
print(len(people))
print(people.keys())
print(people.values())

print(people.get('names',"It doesn't exist"))
print(people)