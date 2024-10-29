###WAYS OF CREATING DICT 
my_dic ={
    "name": "john", "age": 30, "city": "new york"
}   

print(my_dic["city"])

dict() , {}
class_record = {1: {"Sam", "class 6"},
                2: {"lydia Mansah", "class 6"},
                3: {"hassan Musah", "class 6"}
                }
print(class_record[1])

# return all the keys in the dicttionry
print(class_record.keys())
print(class_record.values())
print("--------------------------------------------")
######### To add a new record you need this sytax
class_record [4] = {"sharkdrack", "class 6"} 
print(class_record)

print("----------------------------------------------------------")

# iteration of dictionory
var = class_record.keys()
for each_item in var:
    print(class_record [each_item])
print("--------------------------------------------------------------")

############### Create an empty class register.

class_reg = []
for each_user in range(1, 6):
    # ask for the user fullname
    user_input = input( "Enter your fullname: ")
    # stoer the user fullname in class_reg
    class_reg.append(user_input)
print(class_reg)













