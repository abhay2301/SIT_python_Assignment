'''Write a program in Python to calculate sum of Fibonacci series.'''

def fabo(n):
    a=-1
    b=1
    for i in range(1,n+1): 
        c=a+b
        a=b
        b=c
        print('Fabonicci Series= ',c)
        
    return 0

num=int(input('Enter no.of term: '))
fabo(num)
