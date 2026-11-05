number=int(input("Enter a number: "))
original=str(number)
reversed_num=original[::-1]
if number>=0 and original==reversed_num:
    print(number,"is a palindrome number.")
else:
    print(number,"is not a palindrome number.")
