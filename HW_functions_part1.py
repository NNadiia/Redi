#convert temperatures between Celsius and Fahrenheit

def get_convertion_choice():
    while True:
        number=input("Please choose: Celsius to Fahrenheit = 1, Fahrenheit to Celsius = 2: ")
        if number =="1" or number =="2":
           return number
        else:
            print ("Error. Please choose 1 or 2 option") 

def get_temperature(): 
    while True:
        temp =input("Please enter the temperature: ")
        try: 
            return float (temp)
        except ValueError:
            print ("Please enter only numbers")

def  calculation (choice, temp):
    if choice =="1": # Celsius to Fahrenheit
        return round((1.8 * temp) + 32, 1) 
    elif choice == "2":  # Fahrenheit to Celsius
        return round (.5555555556 * (temp  - 32), 1)
    else:
        return ("Invalid input, please try again.")
    
def final_result():
    user_choice = get_convertion_choice()
    user_temp = get_temperature()
    result = calculation(user_choice, user_temp)
    if user_choice =="1":
           print(f"The result is {result}°F")
    else:
           print(f"The result is {result}°C")   
final_result()    
    
 
      