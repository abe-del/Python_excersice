# gemechu="Hi I am Gemechu"
# gemechu_age=30
# gemechu_address="piassa"
# gemechu_occupation="software developer"
# print(gemechu,"I am",gemechu_age,"years old.")
# print('I live in',gemechu_address)
# print('I am a',gemechu_occupation)
#introduction=input('Enter yourintroduction:')
#person_age=int(input('Enter your age:'))
#input('Enter your address:') 
#person_occupation=input('Enter your occupation')
#print(introduction,"I am",person_age,"years old")
#print('I live in',person_address)

#print('I am a',person_occupation)
#empty array type
numbers=[]
for i in range(0,5):
    input_number=int(input("Enter number",i,":"))
    numbers.append(input_number)
    print (numbers)

#I am trying to accept the four numbers
number_one=int(input("Insert the first number:"))
number_two=int(input("Insert the second number:"))
number_three=int(input("Insert the third number:"))
number_four=int(input("Insert the fourth number:"))

#display the result
choice = input("Enter your prefered calculation:average, multiply  or sum :")


#calculate the average
average=(number_one+number_two+number_three+number_four)/4
#calculate the sum
sum=number_one+number_two+number_three+number_four

multiple=number_one*number_two*number_three*number_four
#display the result based onthe condition/choice
#if(choice=="average"):
 #   print("The average of the number:",average)
#elif(choice =="sum"):
    #print("The sum of the number:",sum)
#elif(choice =="multiply"):
    #print("The multiplication of the number:",multiple)
#else:
    #print(average,sum,multiple)


