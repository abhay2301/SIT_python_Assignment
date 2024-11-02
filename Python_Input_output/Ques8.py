
Num=int(input("Enter number= "))
rev=0
rem=0
while Num > 0:
    rem=Num%10
    rev=rev*10 + rem
    Num //10
print('Reverse of Number=',rev)
