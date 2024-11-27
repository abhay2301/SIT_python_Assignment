'''If the three sides of a triangle are entered through the keyboard, write a program to check 
whether the triangle is isosceles, equilateral, scalene or right angled triangle. 

'''
def right_angle(a,b,c):
    if  a**2+b**2==c**2 or a**2==b**2+c**2 or b**2==a**2+c**2:
        return True
    return False
def classify_triangle(a,b,c):
    if a == b == c:
        return "Equilatral Triangle"
    elif a==b or b==c or c==a:
        return "Isosceles Triangle"
    elif right_angle(a,b,c):
        return "Right angle Triangle"
    else:
        return "scalene Triangle"

a=int(input("Enter the first Side: "))
b=int(input("Enter the second Side: "))
c=int(input("Enter the third side: "))

triangle=classify_triangle(a,b,c)
print(f"This Triangle is {triangle}")