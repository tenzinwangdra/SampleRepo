x=int(input("Enter your age:"))
y=input("Are you a student? (yes/no): ").lower()

if x<=12 or ((x>=13 and x<=18) and y=="yes"):
    print("You are eligible for a discount on the movie ticket.")
else:
    print("You are not eligible for a discount on the movie ticket.")
    
