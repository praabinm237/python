# adding new person
def add_person(people):
    new_person={
        'name': input('Enter name :'),
        'age' : int(input('Enter age :')),
        'gender' : input('Enter gender :')
    }
    people.append(new_person)
    print('Person added successfully!!')
    return people

# updating information of existing person
def update_person(people):
    name_to_update = input('Enter the name of the person who want to update')
    for person in people:
        if person['name'].strip().lower()==name_to_update.strip().lower():
            person['name']=input('Enter new name :')
            person['age']=int(input('Enter new age :'))
            person['gender']=input('Enter new gender :')
            print('Person updated successfully')
            return people
    print('Person not found')
    return people

#deleting existing person
def delete_person(people):
    name_to_delete=input('Enter name you want to delete :')
    for person in people:
        if person['name'].strip().lower()==name_to_delete.strip().lower():
            people.remove(person)
            print('Person deleted successfully')
            return people
    print('Person not found')
    return people

# display list of people
def display_people(people):
    if people:
        for person in people:
            print(f'Name = {person['name']}, Age = {person('age')}, Gender = {person('gender')}')
    else:
        print('No people to display') 

def star(func):
    def wrapper():
        print('               ***************************               ')
        func()
        print('               ***************************               ')
    return wrapper
        
# Main function
@star
def main():
    people=[]
    while True:
        print('Options :')       
        print('1. Add person')
        print('2. Update person')
        print('3. Delete person')
        print('4. Display all people')
        print('5. Exit')
        choice=input('Enter option :')
        
        if choice=='1':
            people=add_person(people)
        elif choice=='2':
            people=update_person(people)
        elif choice=='3':
            people=delete_person(people)
        elif choice=='4':
            people=display_people(people)
        elif choice=='5':
            print('Exiting the program')
            break
        else:
            print('Invalid option. Please try again')
            main()
        
main()
        
        
        
        
        