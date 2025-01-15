'''Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and 
continue) '''


'''
#Method:1
print("Prime number 1 to 300: ")
for num in range(2,301):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=' ')
          
'''
number=int(input('Enter the Number: '))
for num in range(2,number):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end='  ')
        