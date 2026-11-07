password=input("Enter the password  ")
has_upper=any(char.isupper() for char in password)
has_lower=any(char.islower() for char in password)
has_digit=any(char.isdigit() for char in password)
if len(password)<6:
    print("Weak Password")
elif len(password) >=8 and has_upper and has_lower and has_digit :
    print("Strong Password")
else:
    print("Medium Password")