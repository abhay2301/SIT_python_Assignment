''' An Insurance company follows following rules to calculate premium. 
• If a person's health is excellent and the person is between 25 and 35 years of age and lives in 
a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot 
exceed Rs. 2 lakhs. 
• If a person satisfies all the above conditions except that the sex is female then the premium is 
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh. 
• If a person's health is poor and the person is between 25 and 35 years of age and lives in a 
village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 
10,000. 
• In all other cases the person is not insured. 
Write a program to output whether the person should be insured or not, his/her premium rate and 
maximum amount for which he/she can be insured. '''


health=input("Enter the health condition(excellent(e)/poor(p)): ").lower()
age=float(input("Enter your age: "))
location=input("Enter your Location(city(c)/village(v)): ").lower()
sex=input("Enter your gender(male(m)/female(f): ").lower()
if health=="excellent" and 25<=age<=35 and location=="city":                   #{e/E= Excellent} and {c/C=   City}
    if sex=="male":
        premium_rate=4
        policy_amount=200000
        print(f"Incured with the rate of {premium_rate} and the policy amount will be {policy_amount}")
    elif sex=="female":
        premium_rate=3
        policy_amount=100000
        print(f"Incured with the rate of {premium_rate} and policy amount will be {policy_amount}")
    else:
        print("Not Incured")
        
elif health=="poor" and 25<=age<=35 and location=="village":
    sex=="male"
    premium_rate=6
    policy_amount=10000
    print(f"Incured with the rate of {premium_rate} and the policy amount will be {policy_amount}")
else:
    print("Not conered any Insurance")
