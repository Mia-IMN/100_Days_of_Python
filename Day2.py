#This is a tip calculator app. 
#It's meant to calculate the percentage of your bill you'd love to give as a tip.

#Introductory message
print("Welcome to the tip calculator.")

#Getting total bill amount from user
total_bill = input("What was the total bill? $")

#Getting desired tip percentage from user
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

#Getting input on whether the bill is to be split between more than 1 person
bill_split_parts = input("How many people to split the bill? ")

#Calculating the total tip by multiplying the desired tip percentage with the total bill amount and dividing by 100
#Note: since the input function takes in data as strings, I had to convert it to float 
#I used float and not int because I didn't want to lose the cents(the numbers after the decimal point)
total_tip = (float(total_bill) * float(percentage_tip))/100

#Calculating the amount each person involved in the bill spliting has to pay
individual_bill = (float(total_tip) + float(total_bill))/float(bill_split_parts)

#Rounding up the individual bill to two decimal place for clarity
rounded_up_individual_tip = round(individual_bill, 2)

#Yay!! The final result using f-strings...
print(f"Ëach person should pay: ${rounded_up_individual_tip}")