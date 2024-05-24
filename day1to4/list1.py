# x = list((1,2,3,4))
# print(x)
# print(tuple(x))


fruits=(
    "apple",
    "banana",
    "orange"
)
print(type(fruits))

print('converting tuple to list')

fruits=list(fruits)
print(type(fruits))
fruits[0]="kiwi"

fruits=tuple(fruits)
print(fruits)
print(type(fruits))

