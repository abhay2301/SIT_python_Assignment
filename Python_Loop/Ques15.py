'''When interest compounds q times per year at an annual rate of r % for n years, the principle p 
compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r, 
n & q and calculate the corresponding as. 
a =p(1+r/q)^np  '''

set=10

for i in range(set):
    print(f"set{i+1}:")
    
    
    
    p=float(input("Enter Your Priciple (p): "))
    r=float(input("Enter interest rate in % (r): "))/100
    q=int(input("Enter the times compound interest per year (q): "))
    n=int(input("enter time(t): "))
    
    a =p*(1+r/q)**(n*q)
    print(f"The compound amount(A):{a:.2f}")


