'''Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each 
digit of the number is equal to the number itself, then the number is called an Armstrong number. 
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ) '''


num=int(input("Enter the number between 1 to 500 : "))
if num>0 and num<500:
    rem=0
    sum=0
    
    while num!=0:
        rem=num%10
        num=num//10
        
        sum=sum+(rem**3)
    print('Armstrong Number=',sum)
    if(num==sum):
        print('This is a Armstrong Number')
    else:
        print("This is not a Armstrong Number")    
else:
    print("You press wrong number")