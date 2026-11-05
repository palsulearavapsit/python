n = int(input("enter a number to find its factorial"))
fact = 1
if(n<0):
    print("factorial not possible")
elif(n == 0):
    print("factorial is 0")
else:
    for i in range(2 , n+1):
        fact *=i
    print("factorial is: " , fact)

