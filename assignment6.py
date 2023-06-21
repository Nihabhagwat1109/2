#function named ds with parameters roll_no and name.
roll=int(input("enter your roll number"))
nme=input("enter your name:")
ds={
    "rollno:": roll,
    "name":nme
}
print(ds)    
# Add parameters to a tuple
my_tuple = (ds)
print("Tuple:", my_tuple)

# Add parameters to a set
my_set = set()
my_set.add(ds)
my_set.add(ds)
print("Set:", my_set)

# Add parameters to a dictionary
my_dict = {}
my_dict['Roll No'] = ds
my_dict['Name'] = ds
print("Dictionary:", my_dict)
# Change values during runtime
roll_no_new = input("Enter new Roll No: ")
name_new = input("Enter new Name: ")
ds[0] = roll_no_new
ds[1] = name_new
my_tuple = (roll_no_new, name_new)
my_set.remove(ds)
my_set.add(roll_no_new)
my_set.remove(ds)
my_set.add(name_new)
my_dict['Roll No'] = roll_no_new
my_dict['Name'] = name_new

# Delete data structures
del ds
del my_tuple
del my_set
del my_dict