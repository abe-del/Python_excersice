#array searching
numbers = []
#accept the collection from users
user_input = input("Enter the numbers separeted by comma:")
input_values=user_input.split(",")
for values in input_values:
    numbers.append(int(values.strip()))
print(numbers)


target_value =int(input("Enter the number to search:"))
# Initialize index and boolean flag
index=0
found =False
#while loop condition based onthe booleanvalue found
while index < len(numbers)and not found:
    if numbers[index]==target_value:
        found =True #set found to True if the target
    index+= 1 #move to the next index
# check if the value was found and print the result
if found:
    print(f"value {target_value}found in the array.")
else:
    print(f"value {target_value} not found in the array.")

