'''Enter ram age:12
Enter Shyam age: 1
Enter Ajay age: 16
Shyam is the youngest person'''

Ram=int(input('Enter ram age:' ))
Shyam=int(input('Enter Shyam age: '))
Ajay=int(input('Enter Ajay age: '))
youngest_age=Ram
youngest_person='Ram'
if Shyam<youngest_age:
    youngest_age=Shyam
    youngest_person = 'Shyam'
if Ajay<youngest_age:
    youngest_age=Ajay
    youngest_person='Ajay'
print(youngest_person,'is the youngest person')
