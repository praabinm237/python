person = {
    "name":"Ram",
    "age" : 20,
    "gender" : "male",
    "hobbies" : [
        "singing",
        "dancing"
    ],
    "family" : {
        "father" : "Shyam",
        "mother" : "Gita",
    },
    "friends":[
        {
            "name":"John",
            "age" : 12
        },
        {
            "name":"Hari",
            "age" : 12
        },
        {
            "name":"Rameshwor",
            "age" : 12
        }
    ]
}

# print(person["hobbies"][0])
# print(person["family"]["father"], person["family"]["mother"])
# print(person["friends"][1]["name"])
# print(person["friends"][1]["age"])
print(f"""
      My name is {person['name']}
      My age is {person['age']}
      My father's name is {person['family']['father']}
      My mother's name is {person['family']['mother']}
      My hobbies are {person['hobbies'][0]} and {person['hobbies'][0]}
      My friends are {person['friends'][0]['name']}, {person['friends'][1]['name']} and {person['friends'][2]['name']}
      """
      )
# print(f"""
#       My name is {person['name']}
#       My age is {person['age']}
#       My father's name is {person['family']['father']}
#       """
# )