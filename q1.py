person = {
    'first_name': 'Sadia',
    'last_name': 'Razzaq',
    'age': 20,
    'city': 'karachi',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
#Adding key value pair
person.update(Qualification = 'Intermediate' )
#Updating Qualification
person.update(Qualification = 'high academic level')

del person['Qualification']
