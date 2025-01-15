'''Write a program in Python to calculate combinatoric C(n,r) using function.'''

def fact(num):
    f=1
    while num>0:
        f=f*num
        num=num-1
    return f
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
print(fact(n))
print(fact(r))
print("The value of C(n,r):",fact(n)//(fact(r)*fact(n-r)))
