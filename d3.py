#If-Else statement 

age = int(input("Enter your age in numubers: "))
op = int(input("Now choose what you want from given options?\n1. aligable for pan card?\n2. Can I marriage?\n"))

# for 1st option.
if(op==1):
    if(age>=18):
        print("you are aligable for pan card.")
    elif(age>=0 and age<18):
        print("you aren't aligable for pan card.")
    else:   
        print("opps!!!! \n Enter valid age.")

elif(op==2):
    if(age>=0 and age<24):
        print("For now i think you need to focus on your goal (O.O)\nOthervise it's your choise.....")
    elif(age>=24):
        print("Yes, you can but why you want to problems. (>.<)")
    
