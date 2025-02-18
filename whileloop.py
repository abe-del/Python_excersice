#accept the numbers form
numbers=[]
counter=0
while counter <4:
    number_input=int(input("Enter the number:"))
    numbers.append(number_input)
    counter=counter+1
choice = input("enter your prefered calculation;sum,average or multiply:")
#calculate the sum of numbers
sum=numbers[0]+numbers[1]+numbers[2]+numbers[3]
#calculate the average
average=sum/4
#calculate the multiplication of the numbers
multiple=numbers[0]*numbers[1]*numbers[2]*numbers[3]
#displayed the calculation the user chose
if (choice== 'sum'):
    print("the sum of the number:",sum)
elif(choice =='average'):
    print('The average of the numbers',average)
elif(choice=='multiply'):
    print("the multiplication of the numbers:",multiple)
else:
    print(sum,multiple,average)