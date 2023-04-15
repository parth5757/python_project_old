A = int(input("Enter the amount ,which you want to apply gst:"))
print("1)FOOD 2)CLOTHES 3)ELECTRICAL DEVICES 4)OTHER GOODS")
B = int(input("Enter choice : "))
if B == 1: print("GST RATE 5% = ",A * 5/100 ,"\nPAYABLE AMOUNT:",A + A * 5/100 )
elif B == 2: print("GST RATE 12% = ",A * 12/100 ,"\nPAYABLE AMOUNT:",A + A * 12/100)
elif B == 3: print("GST RATE 18% = ",A * 18/100 ,"\nPAYABLE AMOUNT:",A + A * 18/100)
elif B == 4: print("GST RATE 28% = ",A * 28/100 ,"\nPAYABLE AMOUNT:",A + A * 28/100)
else:
 print("enter valid choice")