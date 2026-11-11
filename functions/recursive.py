#factorial with normal code
# fact = 1
# n = int(input("enter a number: "))
# for i in range(1 , n+1 , 1):
#     fact = fact * i
# print(f"factorial is {fact}")

#factorial with recurrive funciton
def fact(n):
    if (n<0):
        print("enter  a number greater than 0")
    elif((n == 0) or ( n == 1)):
        return 1
    else:
        return n*fact(n-1)

n = int(input("enter a num: "))
print(f"factorial is {fact(n)}")

#fibonacci with normal code
#0 1 1 2 3 5
# n = int(input("Enter the number of terms: "))
# a , b = 0 , 1
# for i in range(0 , n , 1):
#     print(a , end=" ")
#     c = a + b
#     a = b
#     b = c

#fibonacci using recursion
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("enter the no of terms"))
for i in range(n):
    print(fibo(i) , end=" ")