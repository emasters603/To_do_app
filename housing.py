#annualized $ or %

inflation = .025
downpayment = .2
home_insurance = 1200
upkeep = .015
closing_costs = .1
capital_gains =.25
buying_cost = .04
renter_insurance = 200
security_deposit = 2000
property_tax = .01



def rent_buy():
	rental_cost = int(input("monthly rental price"))
	house_cost =  int(input("total house cost"))
	downpayment = .2 * house_cost
	finance_rate = int(input("percent on loan for house"))
	length = int(input("how long is the loan for"))
	joint_income = int(input("joint-income")) 
	house_sum = house_cost*(1+buying_cost)
	payment = house_cost - downpayment
	house = []
	rent = []
	investment = downpayment*.5
	for i in range(0, length*12):
		count =1
		house_month = ((house_cost - downpayment)/(12*length - count)) * ((1 + upkeep/12 + property_tax/12))*((1 +.025/12)**count) + home_insurance/12*((1 +.025/12)**count)
		house_cost = (house_cost - payment - house_cost/(12*length - count))*(1+finance_rate/12)**count 
		if house_month > (joint_income*.3)/12:
			print("The house is too expensive")
			break
		else:	
			house.append(house_month) 
			avg_house_month = sum(house)/len(house) + house_sum/count + (downpayment/count)
			print("H:" ,avg_house_month)
			monthly_rent = (rental_cost + 50 ) * ((1+ .025/12)**count) 
			rent.append(monthly_rent)
			if rental_cost > house_month or rental_cost > (.25*joint-income):
				print("Sorry! Find some cheaper rent")
				break
			else:
				investment = ((house_month - monthly_rent)+investment)((1+.06/12)**count)
				avg_rent = (sum(rental_cost)+ security_deposit/(1+.025/12)**count )/len(rent)
				print("R:" ,avg_rent)
				print("Investing the difference over this time period made")
				house_value = (house_cost * (1+.025/12)**count )*.9	
				print(house_value)
				count +=1

rent_buy()
	
