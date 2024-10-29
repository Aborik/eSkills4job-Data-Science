############### Create an empty class register.
class_reg = []
reg_count = int(input("Enter the number of student to register: "))
for each_user in range(1, reg_count + 1):
    # ask for the user fullname
    user_input = input( "Enter your fullname: ")
    # stoer the user fullname in class_reg
    class_reg.append(user_input)
print(class_reg)