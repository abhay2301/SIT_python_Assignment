''' A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 
6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 
days your membership will be cancelled. Write a program to accept the number of days the 
member is late to return the book and display the fine or the appropriate message.'''


days_late=int(input('Enter the returning days: '))
if(days_late==0):
    print("Returning book on time, so no need to pay late fine")
elif 0<days_late<=5:
    fine=0.5
    print('late fine is: ',fine)
elif(5<=days_late<=10):
    fine=1
    print('Late Fine is: ',fine)
elif(11<=days_late<=30):
    fine1=5
    print("Late fine is: ",fine1)
else:
    print('Memberships will be cancelled')    

