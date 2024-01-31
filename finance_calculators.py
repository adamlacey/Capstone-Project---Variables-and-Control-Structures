import math

# User has 2 options to input data relating to investments or bonds. 

def display_menu():
    print("investment - to calculate the amount of interest you'll earn on your investment bond")
    print("bond       - to calculate the amount you'll have to pay on a home loan \n")

# User can only enter varialbe which is the same as the above strings. \
# Otherwise, an error will be printed.

def obtain_users_choice():
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    user_choice = choice.strip().lower()
    return user_choice

# Each statement is printed below once user enters investment or bond decision.
# Based on what the user enters, the questions will be asked to determine the \
# end calculation of either option.

def calculate_investment():
    deposit = float(input("How much money are you depositing?: £ "))
    interest_rate = float(input("What is the interest rate? Please enter a percentage: "))
    years = float(input("How many years are you planning on investing?: "))
    interest_type = input("Please enter either 'simple' or 'compound' for the interest type: ").lower()
    interest_division = interest_rate/100
    
# The calculations below determine the total investment value for both \
# compound and simple interest.
    
    if interest_type == "simple":
        simple_interest = deposit * (1 + interest_division * years)
        print("The total investment value is: £ ", round(simple_interest))
    elif interest_type == "compound":
        compound_interest = deposit * math.pow((1 + interest_division), years)
        print("The total investment value is: £ ",round(compound_interest))
    else:
        print("Error: your must pick 'simple' or 'compound'.")
 
# Questions below ask the user to input value of house, interest rate and \
# how long the payment will take to be paid. 
    
def bond_repayment_calculation():
    house_value = float(input("How much is the value of the house?: "))
    interest_rate = float(input("What is the interest rate?: "))
    monthly_rate = (interest_rate / 100) / 12
    bond_repay = float(input("How many months do you plan on taking to repay the bond?: "))
    
# The bond repayment is calculated based upon users answers from the \
# following questions above.
    
    bond_repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (- bond_repay))
    print("The repayment total is: £ ", round(bond_repayment))
    
def main():
    display_menu()
    user_choice = obtain_users_choice()

# Showcasing to the user that either investment or bond has been chosen.

    if user_choice == "investment":
        print("You have chosen: investment\n")
        calculate_investment()
    elif user_choice == "bond":
        print("You have chosen: bond\n")
        bond_repayment_calculation()
    else:
        print("Error: You must pick 'investment' or 'bond'.")

if __name__ == "__main__":
    main()