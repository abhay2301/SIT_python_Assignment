'''Location of C: 10
Location of D: 20
After Interchange: C= 20 D= 10'''

C=int(input('Location of C: '))
D=int(input('Location of D: '))
C,D=D,C
print('After Interchange: C=',C,'D=',D)
