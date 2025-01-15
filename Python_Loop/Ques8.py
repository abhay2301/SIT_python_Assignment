'''Write a program to find the octal equivalent of the entered number.'''
num=int(input("Enter Decimal Number: "))
rem=0
#octal_num=00
while num!=0:
    rem=num%8
    num1=num//8
    
print("Octal number= ",rem,num1)
