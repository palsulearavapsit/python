score = int(input("enter you score from 0 to 100: "))
if(score < 33):
    print("bad")
elif((score>=34)and(score<66)):
    print("nuetral")
elif((score>=67)and(score<=100)):
    print("good")
else:
    print("enter a valid score befrom 0 to 100")