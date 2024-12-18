# print("Welcome to the Band Name Generator.")
# city = input("Which city did you grow up in?\n")
# pet = input("What is the name of a pet?\n")
# print("Your band name could be " + city + " " + pet)

# Total kg calculation of cocoa beans:
print("Input the number of kg and moisture content to know the Net Weight")
Gross_Weight = float(input("Total Gross Weight\n"))
Percentage_Moisture = float(input("Percentage Moisture\n"))
No_of_bags = int(input("No of Bags:\n"))
Weight1=Gross_Weight-No_of_bags
Moisture_content = Percentage_Moisture - 7
kg_reduction = Moisture_content/100*Weight1
Weight = Weight1-kg_reduction
Net_Weight = round(Weight, 2)
print(f'Net Weight is: {Net_Weight}Kg')
