print("Newton's Second Law of Motion")
print("Select the ,missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option numner for the missing value")

if missing_value_choice == "1":
    a = float(input("Enter Acceleration (a): "))
    F = float(input("Enter Force (F): "))
    m = F / a
    print(f"Mass (m) = {m}")
elif missing_value_choice == "2":
    m = float(input("Enter masss (m): "))
    F = float(input("Enter force (F): "))
    a = F / m
    print(f"Acceleration (a) = {a}")
elif missing_value_choice == "3":
    m = float(input("Enter masss (m): "))
    a = float(input("Enter acceleration (a): "))
    F = m * a
    print(f"Force (F) = {F}")   
else:
    print("Invalid option for the missing value.")
