'''Write a program Python to calculate l.c.m using while loop. '''


def calculate_lcm(a,b):
    greater=max(a,b)
    
    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))
    
lcm=calculate_lcm(num1,num2)
    
print(f"The LCM of {num1} and {num2} is {lcm}")
    
    