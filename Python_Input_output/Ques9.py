'''Enter four digit Number: 4655
sum of first and last= 9'''

num=int(input("Enter four digit Number: "))
if 1000<= num <=9999:
    last_digit=num%10
    first_digit=num//1000
    sum=last_digit + first_digit
    print('sum of first and last=',sum)

