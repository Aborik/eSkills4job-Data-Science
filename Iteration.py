# generate the numbers below
for i in range(1, 15):
    print(i)

# generate seq of even number b/n 1 and 15 []
for x in range( 2, 15, 2):
    # 2 in the set is the step
    print( x)

# generate seq of even number b/n 15 and 4 (revers form)
for x in range( 15, 4, 2):
    print( x)

class_reg = [ 'Nat', 'Jul', 'Oscar', 'Tah']  
for each_item in class_reg:
    print(each_item)

user_name = input( "Enter your name: ")
# Dispalying the name three times
for each_name in range(1, 4):
    print("Your nama is: ", user_name)

user_name = input("Enter your name: ")
nath_1 = int( input(" Enter your number: "))
for each_time in range (1, nath_1+1):
    print("You name is: ", user_name)


    user_name = input( "Enter you name: ")
name_num = int( input("Enter your number: "))
if ( name_num < 10):
    for each_number in range(1, name_num+1):
        print( user_name )
else: 
    if(name_num > 10):
        for each_number in range(1, 4):
            print( "Too high")


# Q 18
user_input = int(input( " Enter a number: "))
if (user_input < 10):
    print("Too low")
elif (10> user_input < 20):
    print("Correct")
else:
     print("Too high")


again = "yes"
while (again == "yes"):
    print("Hello")
    again = input("Enter yes or no: ")

    total = 0
while ( total <= 10):
    print( "Conunter => ", total)
# control for while loop is a counter
    print("Hello world")
    total = total + 1
print("Goodbye")



print(" CLASS ATTENDENC REGISTER")
attendece = input("Have you registered or not: ")
while ( attendece == "no"):
    username = input("Enter your name to register: ")
    print( "Confirm Name", username)
    ### Loop control
    attendece = input("Have you registered or not: ")


user_input = 0
while (user_input < 5):
    user_input = int(input("Enter a number: "))
    # while control
print("The last number you entered was a number")