print("=========Temperature Converter=========")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    c=float(input("Enter temperature in Celsius: "))
    f=(c*9/5)+32
    print(f"{c}°C is equal to {f}°F")
elif choice == "2":
    f=float(input("Enter temperature in Fahrenheit: "))
    c=(f-32)*5/9
    print(f"{f}°F is equal to {c}°C")
else:
    print("Invalid choice. Please select 1 or 2.")