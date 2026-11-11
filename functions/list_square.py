#paramters for function are-->
# list - lst
# tuple - t
#dictionary - d
# array - arr  and we use "import arr"
#isinstance is used to check datatypes - isinstance(x, list), isinstance(x, dictionary), isinstance(x, int)

def list_square(lst):
    sqlt =[]
    for i in range(len(lst)):
        #if((type(list[i]) == int) or (type(list[i]) == float)):
        if isinstance(lst[i], (int, float)):
            sqlt.append(lst[i]**2)
        else:
            sqlt.append(lst[i])
    print(sqlt)
list_square(["arav", 2, 2.4, True])