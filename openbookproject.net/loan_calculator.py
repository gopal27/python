#!/usr/bin/python

from sys import argv

script = argv


#Loan I = P X R X T
def calculate_loan_payments(principal, interest_rate, term_in_years):
    #This method calculates the loan and prints the payment schedule

    interest = int(principal * interest_rate * term_in_years)
    
    payment = principal + interest
    monthly_payment = int(payment / (term_in_years * 12))

    print "Amount borrowed:",principal
    print "Total interest:",interest

    
    print "Pymt#\t\tAmt Paid\t\tRemaining Bal"
    print "----------------------------------"
    print "0\t\t$0.00\t\t",payment
 
    pymt = 1;
    while payment > 0:
      payment = payment - monthly_payment
      print pymt,"\t\t$",monthly_payment, "\t\t", payment
      pymt = pymt + 1


print "Loan Calculator"

while True:
    amt = input("Amount Borrowed: ")
    interest_rate = input("Interest Rate: ")
    term_years = input("Term (years): ")

    calculate_loan_payments(amt * 100, interest_rate/100, term_years)
  

 
