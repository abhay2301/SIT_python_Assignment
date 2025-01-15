''' Write a program to enter the numbers till the user wants and at the end it should display the count 
of positive, negative and zeros entered?'''


positive_count=0
negetive_count=0
zero_count=0
#num=float(input("Enter the number: "))
while True:                                         #while loop for infinte time
    
    user=input("Enter number (or type to'stop' to finish) ")
    if user.lower()=="stop":
        break
    
    num=float(user)
    if num>0:
        positive_count+=1
    elif num<0:
        negetive_count+=1
    else:
        zero_count+=1
    
    
print("Total Positive Number= ",positive_count)
print("Total Negetive Number= ",negetive_count)
print("Total Number of Zero= ",zero_count)
