print("School Administration Program")
student_name = ["student name: "]
student_id = ["student id: "]
student_dob = ["student DOB: "]
student_bloodgroup  = ["student blood group: "]
student_address = ["student address: "]
student_phno = ["student phone number: "]
parent_name = ["student parent name: "]
parent_mobileno = ["student parent mobile number: "]
name = input("enter your name : ")
id = input("enter your id : ")
dob = input("enter your dob : ")
bloodgroup = input("enter your bloodgroup : ")
address = input("enter your address : ")
phno = input("enter your Phone number : ")
parent_name1 = input("enter your parent_name : ")
parent_mobileno1 = input("enter your parent_mobile number : ")
student_name.append(name)
student_id.append(id)
student_dob.append(dob)
student_bloodgroup.append(bloodgroup)
student_address.append(address)
student_phno.append(phno)
parent_name.append(parent_name1)
parent_mobileno.append(parent_mobileno1)
target={39:None, 91:None, 93:None}
print(str(student_name).translate(target))
print(str(student_id).translate(target))
print(str(student_dob).translate(target))
print(str(student_bloodgroup).translate(target))
print(str(student_address).translate(target))
print(str(student_phno).translate(target))
print(str(parent_name).translate(target))
print(str(parent_mobileno).translate(target))
