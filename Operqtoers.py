
# aks for two number if the fisrt one is larger the secon number display the second number
#  and fisrt number otherwise.

# asking for two number and convert them to int
first_number = int(input("Enter fisrt number: "))
second_number = int(input("Enter second number: "))
# Test for the condition and make a decision.
if (first_number > second_number):
   print( second_number, first_number) 
else:
   print(first_number, second_number)


number1 = int(input("Enter fisrt number: "))
# # Test for the condition and make a decision.
if ( number1 > 20):
    print( "Too High")
else:
    print("Thank you")


user_input = int(input("Enter a number b/n 10 and 20:   "))
# CONDITION FOR TO DECISED b/n 10 T0 20
if ((user_input>=10) and (user_input<= 20)):
    print("Thank you")
else:
    print("Incorrect Answer")


user_input = input("Enter favorite colour:  ")
if (user_input == "red") or ( user_input==  "Red") or (user_input == "RED"):
  print( "I like red")
else:
  print( "I don't like", user_input)
    