'''Write a program in Python to calculate H.C.F using while loop.'''


def calculate_hcf(a,b):
    while b:
        a,b=b,a%b
    return a
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd Number: "))
hcf=calculate_hcf(num1,num2)
print(f"HCF of {num1} and {num2} are {hcf} ")

