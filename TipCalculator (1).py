#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Welcome the user
print("Welcome to the tip calculator!\n")

#Gather the input
total_bill=input("What was your total bill? $")

#typecast to float
new_total_bill=float(total_bill)

#find the amount of tip to be given
tip=int(input("What percentage tip would you like to give? 10, 12 or 15? "))

#find the number of people to split the bill
people=int(input("How many people want to split the bill? "))


#find the percentage tip and the amount to be split
value_of_tip=(tip/100) + 1
new_total=new_total_bill* value_of_tip
result=new_total/people
round_result = "{:.2f}".format(result)
print(f"Each person should pay: ${round_result}")