'''Write a program in Python to check whether an inputted number is palindrome.'''

def palindrome(n):
    rev=0
    while n>0:
        
        #rem=0
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
def number():
    num=int(input("Enter the number: "))
    numbers=palindrome(num)   
    if num==numbers:
        print(f"This number is palindrome:{num}")
    else:
        print(f"This number is not palindrome:{num}")
        
number()