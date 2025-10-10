from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

# > python tester.py
# Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
# $>

# student = Student(name = "Edward", surname = "agle", id = "toto")
# print(student)

# > python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id'
# $>
