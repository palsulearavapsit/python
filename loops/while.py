n = int(input("enter a number which  greater than 0  , whose factorial we need to find"))
fact = 1
while(n>0):
    fact *=n
    n -=1

print(fact)