'''Write a program to add first seven terms of the following series using a for loop: 1+2/2!+3/3!.....n/n!'''

num=int(input('Enter the number: '))
fact=1
for i in range(1,num+1):
        fact*=i
print(fact)