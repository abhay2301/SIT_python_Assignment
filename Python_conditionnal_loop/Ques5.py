'''Enter a five number: 12345
Reverse Number=  54321
'''

num=int(input('Enter a five number: '))
if 9999<num<100000:
    rem=0
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print('Reverse Number= ',rev) 
else:
    print('You Enter Invalid Number')


