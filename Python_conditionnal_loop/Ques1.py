'''Enter Cost Price: 100
Enter Selling Price: 50
loss
loss=  50'''

cp=int(input('Enter Cost Price: ')) #(cp means cost price)
sp=int(input('Enter Selling Price: ')) #(sp means selling price)
if sp-cp>0:
    
    print("profit")
    print("profit= ",sp-cp)
    
else:
    print("loss")
    print("loss= ",cp-sp)


