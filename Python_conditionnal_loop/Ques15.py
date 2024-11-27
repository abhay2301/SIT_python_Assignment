''' If the three sides of a triangle are entered through the keyboard, write a program to check 
whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than 
the largest of the three sides.


'''
def is_triangle_valid(a,b,c):
    return (a+b>c) and (a+c>b) and (b+c>a)
side1=float(input('Enter the A side of triangle: '))
side2=float(input('Enter the B side of triangle: '))
side3=float(input('Enter the C side of triangle: '))

# check triangle is valid or not
if is_triangle_valid(side1,side2,side3):
    print('This is Triangle')
else:
    print('This is not a Triangle')
    