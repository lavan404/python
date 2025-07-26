a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print("1 for Add")
print("2 for Subtract")
print("3 for Multiply")
print("4 for Divide")
c = int(input("Choose an operation 1/2/3/4: "))

if c ==1:
    print (a + b)
elif c ==2:
    print(a-b)
elif c == 3:
    print (a*b)
elif c ==4:
    print(a/b)
else:
    print("Enter a valid input !!")
