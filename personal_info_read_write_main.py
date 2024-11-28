first_name = []
last_name = []
middle_name = []
birthday = []


while True:
    
    user_input = str(input("Please enter your first name : "))
    first_name.append(user_input)
    
    user_input = str(input("Please enter your last name : "))
    last_name.append(user_input)
    
    user_input = str(input("Please enter your middle name : "))
    middle_name.append(user_input)
    
    user_input = str(input("Please enter your birthday  : "))
    birthday.append(user_input)
    
    break

with open("user_output.txt", "w") as output:
    output.write(str(first_name))
    output.write(str(last_name))
    output.write(str(middle_name))
    output.write(str(birthday))

print(f"{first_name}")
print(f"{last_name}")
print(f"{middle_name}")
print(f"{birthday}")

