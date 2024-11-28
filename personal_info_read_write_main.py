#initialize all the arrays we'll be using
first_name = []
last_name = []
middle_name = []
birthday = []
#i'm gonna use an array to store the correect answers to repeat the loop for convinience
retry_array = ["Y", "N"]

while True: 
    while True:
        try:
            #prompts the user for data
            user_input = str(input("Please enter your first name : "))
            first_name.append(user_input)
            
            user_input = str(input("Please enter your last name : "))
            last_name.append(user_input)
            
            user_input = str(input("Please enter your middle name : "))
            middle_name.append(user_input)
                
            user_input = str(input("Please enter your birthday  : "))
            birthday.append(user_input)       
            
            #this asks the user if they want to repeat the loop
            retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        except:
            break
        
        
        #this is what progresses the loop
        while not retry_input in retry_array:
            retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        #if the user answers "N" the loop will stop
        if retry_input in retry_array[1]: 
                break
            
    break

#this adds all the answers to the txt file
with open("user_output.txt", "w") as output:
    output.write(str(first_name))
    output.write(str(last_name))
    output.write(str(middle_name))
    output.write(str(birthday))