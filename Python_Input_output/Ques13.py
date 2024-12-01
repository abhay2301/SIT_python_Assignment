num=int(input("Enter five digit Number: "))
if 10000<=num<=99999:
    new_num=0
    while num>0:
        rev=0
        rem=num%10
        new_num=new_num*10+((rem+1))
        num//=10
    print('Reverse number= ',new_num,end='\n')
    
    after_rev=0
    while new_num>0:
        number=new_num%10
        after_rev=after_rev*10+number
        new_num=new_num//10
    print("After adding 1 will be=",after_rev)
else:
    print("Please Enter number between 10000 to 99999")
    
