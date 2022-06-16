
print("From 1 to 10, please answer the questions bellow\n")

loan_largeness = int(input("How large is the loan? [1-10]\n>> "))
credit_history = int(input("How good is your credit history? [1-10]\n>> "))
income_highness = int(input("How high is your income? [1-10]\n>> "))
down_payment_largeness = int(input("How large is your down payment? [1-10]\n>> "))

should_loan = False

if (loan_largeness >= 5):
    if (credit_history >= 7 and income_highness >= 7):
        should_loan = True
    elif (down_payment_largeness >= 5):
        should_loan = True
elif (credit_history >= 4):
    if (income_highness >= 7 or down_payment_largeness >= 7):
        should_loan = True
    elif (income_highness >= 4 and down_payment_largeness >= 4):
        should_loan = True

if(should_loan):
    print("Yes, your loan is approved")
else:
    print("No, your loan was not approved")
