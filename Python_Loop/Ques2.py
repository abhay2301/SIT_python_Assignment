'''Write a program to find the factorial value of any number entered through the keyboard'''

def fact(n):
    f=1
    while n!=0:
        f=f*n
        n-=1
    return f
def main():
    n=int(input("Enter the number: "))
    print("Factorial of Number= ",fact(n))
main()