''' 11. Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will 
determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use 
sqrt( ) and pow( ) functions)'''

x=float(input('centre of x: '))
y=float(input('centre of y: '))

x1=float(input('Enter the x-cooridinate: '))
y1=float(input('Enter the y-cooridinate: '))
r=float(input('Enter the radius: '))
d=(x-x1)**2 + (y-y1)**2
a=r**2
if(a>d):
    print('Inside the Circle')
elif(a==d):
    print('On the Circle')
else:
    print('Outside the Circle')
        
