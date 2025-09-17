first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = first_number * second_number

if result > 0:
    sign_description = "positive"
elif result < 0:
    sign_description = "negative"
else:
    sign_description = "positive and negative"

print(f"{first_number} x {second_number} = {result}")   
print(f"The result is {sign_description}.")