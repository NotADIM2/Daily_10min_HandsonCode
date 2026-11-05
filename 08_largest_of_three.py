num=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

if num >= num2 and num >= num3:
    largest = num
elif num2 >= num and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)