arr = []
r_arr = []
n = int(input("enter the number of elements to added in array"))
print("enter the elements ")
for i in range(0 , n , 1):
   arr.append(int(input("enter the "+ str(i)+ " element: ")))
print(arr)
#print("the reveresed array is ")
#for i in range(n-1 , -1 , -1):
#   r_arr.append(arr[i])
#print(arr.reverse())
print(arr[-1])
print(arr[1:4])