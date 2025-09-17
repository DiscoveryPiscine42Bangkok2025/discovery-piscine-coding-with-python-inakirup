def add_one(num):
    num += 1
    return num


my_variable = 5
print(f"Before calling add_one: {my_variable}")
my_variable = add_one(my_variable)
print(f"After calling add_one: {my_variable}")