num=int(input("Enter five digit Number: "))
if 10000<=num<=99999:
    new_num=0
    while num>0:
        rev=0
        rem=num%10
        new_num=new_num+((rem+1)*10)
        num//=10
    print('New number= ',new_num)
