'''Write a program in Python to calculate factorial of a natural number. '''

def fact(n):
        f=1
        while n>0:
                f=f*n
                n-=1
        return f
def series():
        num=int(input("Enter number: "))
        print(f"The Factorial {num} is = {fact(num)}")
series()