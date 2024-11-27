''' Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all the three 
points fall on one straight line. '''

x1=float(input('enter x1 co-oridinate: '))
y1=float(input('enter y1 co-oridinate: '))
x2=float(input('enter x2 co-oridinate: '))
y2=float(input('enter y2 co-oridinate: '))
x3=float(input('enter x3 co-oridinate: '))
y3=float(input('enter y3 co-oridinate: '))
if (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
    print("All three co-ordinate are collinear")
else:
    print("All three Co-oridinate are not collinear")
