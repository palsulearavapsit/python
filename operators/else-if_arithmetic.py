a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
print("1.add")
print("2.subtract")
print("3.multiply")
print("4divide")
print("5.remainder")
print("6.exit")
op = int(input("choose a valid operation"+
               "choose a valid number " +
               "1 or 2 or 3 or 4 or 5 or 6 "))

if(op == 1):
    print(a+b)
elif(op == 2):
    print(a-b);
elif(op == 3):
    print(a*b);
elif(op == 4):
    if(b == 0):
        print("cannot divide by 0")
    else:
        print(float(a/b));
elif(op == 5):
    print(a%b)
elif(op == 6):
    exit;
else:
    print("enter a valid number to perform an operation ")