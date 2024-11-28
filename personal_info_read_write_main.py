#initialize all the arrays we'll be using
first_name = []
last_name = []
middle_name = []
birthday = []
age = []

#i'm gonna use an array to store the correect answers to repeat the loop for convinience
retry_array = ["Y", "N"]

while True: 
    while True:
            #prompts the user for data
            user_input = str(input("Please enter your first name : "))
            first_name.append(user_input)
            
            user_input = str(input("Please enter your last name : "))
            last_name.append(user_input)
            
            user_input = str(input("Please enter your middle name : "))
            middle_name.append(user_input)
                
            user_input = str(input("Please enter your birthday (mm/dd) : "))
            birthday.append(user_input)  
            
            user_input = str(input("Please enter your age : "))
            age.append(user_input)       
            
            #this asks the user if they want to repeat the loop
            retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        
        #this is what progresses the loop
            while not retry_input in retry_array:
                retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        #if the user answers "N" the loop will stop
            if retry_input in retry_array[1]: 
                break
            
    break

#this adds all the answers to the txt file
with open("user_output.txt", "w") as output:
    for i in range(len(first_name)):
        output.write(f"Name: {first_name[i]} {middle_name[i]} {last_name[i]}" )
        output.write(f"\nBirthday : {birthday[i]}")
        output.write(f"\nAge : {age[i]} years old\n\n")
