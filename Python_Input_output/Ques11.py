amount_hundreds=int(input('Enter the withdrawal amount:  '))
total_amount=amount_hundreds*100
notes_100=total_amount // 100
remaining_amount=total_amount % 100
notes_50 = remaining_amount // 50
remaining_amount=total_amount % 50
notes_10=remaining_amount // 10

print("number of 100 denominations=",notes_100)
print("number of 50 denominations= ",notes_50)
print("Number of 10 denomination= ",notes_10)