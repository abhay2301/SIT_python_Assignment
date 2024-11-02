n=int(input('Enter Five Number'))
rem=0
sum=0
while n>0:
    rem=n % 10
    sum+=rem
    #sum=sum*10 + rem
    n//=10
print('sum of number=',sum)

