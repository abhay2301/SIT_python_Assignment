'''Write a program in Python to print sum of all +ve numbers and all -ve numbers.'''

def sum(number):
    positive=0
    negetive=0
    for i in number:
        if i>0:
            positive+=i
        elif i<0:
            negetive+=i
            
    return positive,negetive
def main():
    num=input("Enter the number:").split()
    number=[int (i) for i in num]
    
    positive,negetive=sum(number)
    
    print(f"the sum of positive number:{positive}")
    print(f"the sum of negetive number:{negetive}")

if__name__="__main__"
main()                                                                               