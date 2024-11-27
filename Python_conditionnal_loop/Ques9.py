'''Enter a length: 5
Enter breadth: 4
Area is greater than perimeter'''

length=float(input('Enter a length: '))
breadth=float(input('Enter breadth: '))

perimeter=2*(length+breadth)

area=length*breadth
if area>perimeter:
    print('Area is greater than perimeter')
else:
    print('Area is not greater than perimeter')
