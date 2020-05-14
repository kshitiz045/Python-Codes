print("FRIENDSHIP CALCULATOR".center(140 , "-"))
print("      ")
alpha = "bcdfghjklmnpqrstvwxyz"
score=0
friends_name = input("Enter first name and then enter space and then second name of your friend")
for i in friends_name:
    if i in "aeiou":
        score+=5
    if i in "friends":
        score+=10
    if i in alpha:
        score+=alpha.find(i)
    else:
        score+=0

if(score>100):
    print("Your friendship score is : " , score)
    print("Congratulations , You both are best friends")
else:
    print("Your friendship score is : " , score)
