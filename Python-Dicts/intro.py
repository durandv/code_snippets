student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# IN
# print("courses" in student)

# GET
# print(student.get('coursess', 'NOT'))
# print(student['courses'])


# ADD
# student['phone'] = '5555-5555'

# UPDATE
# student['name'] = 'linda'
# student.update({'name': 'Jane', 'age': 26, 'phone': '123-123'})

# DEL
# del(student['age'])
# age = student.pop('age')
# print(age)

# LOOP
# for key, value in student.items():
#    print(key, value)

print(len(student))
print(student)
print(student.keys())
print(student.items())
