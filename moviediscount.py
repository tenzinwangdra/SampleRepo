x = input("Enter your age:")

y = input("Are you a student? (yes?no):")

if x <= "12" :
    print("You are aligible for a discount on the movie ticket!")

elif (x >= "13" or x <= "18") and y == "yes" :
    print("You are eligible for a discount on movie ticket!")

else:
    print("You are not eligible for a discount on movie ticket!")