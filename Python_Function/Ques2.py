'''Write a program in Python to check if a given number is even or odd using the function.'''

def even_odd(n):
    if n%2==0:
        print('Even')
    else:
        print('Odd')
    return n
num=int(input('Enter the number: '))
even_odd(num)
#print("Number is",Number)

