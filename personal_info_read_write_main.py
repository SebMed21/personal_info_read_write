first_name = []
last_name = []
middle_name = []
birthday = []

retry_array = ["Y", "N"]
retry_input = ""

while True: 
    while True:
        try:
            user_input = str(input("Please enter your first name : "))
            first_name.append(user_input)
            
            user_input = str(input("Please enter your last name : "))
            last_name.append(user_input)
            
            user_input = str(input("Please enter your middle name : "))
            middle_name.append(user_input)
                
            user_input = str(input("Please enter your birthday  : "))
            birthday.append(user_input)       
            
            retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        except:
            break
        
        while not retry_input in retry_array:
            retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        if retry_input in retry_array[1]: 
                break
            
    break

with open("user_output.txt", "w") as output:
    output.write(str(first_name))
    output.write(str(last_name))
    output.write(str(middle_name))
    output.write(str(birthday))