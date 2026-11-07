print("=======Expense Tracker======")
expenses = []
try:
    n=int(input("How Many Expenses youwant to enter? "))
    if n<=0:
        print("Please Enter a positive number of expenses.")
    else:
        for i in range(n):
            a=float(input("Enter Expense amount:"))
            if a<0:
                print("Negative expenses are not allowed")
                break
            expenses.append(a)
        else:
            print("\n======SUMMARY=========")
            print("Total Expenses:",sum(expenses))
            print("AvG Expense",sum(expenses)/len(expenses))
            print("Highest Expenses",max(expenses))
            print("Lowest Expenses",min(expenses))
except ValueError:
    print("Invalid  .please enter valid inputsinput")
    print("Thanks for using Expense Tracker")

