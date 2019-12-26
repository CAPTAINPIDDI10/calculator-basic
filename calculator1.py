print("This a calculator ")
print("you can add,subtract,multiply,divide")
print("Use these keywords for your desired operation \nadd\nsub\nmult\ndiv")
askUser=input("Type what you want to do:")
print("Enter the numbers")
number_1=float(input("Enter first number:"))
number_2=float(input("Enter second number:"))
if askUser=="add":
         add=number_1+number_2
         print("This is the answer",add)
elif askUser=="sub":
         sub=number_1-number_2
         print("This is the answer",sub)
elif askUser=="mult":
         mult=number_1*number_2
         print("This is the answer",mult)
else:
    div=number_1/number_2
    print("This is the answer",div)

print("Programme by Siddhesh")
