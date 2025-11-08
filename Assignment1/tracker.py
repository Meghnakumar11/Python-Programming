#Meghna Kumar
#30-10-2025
#Daily Calorie Tracking Console App
from datetime import datetime
print("welcome to the daily calorie tracker which makes it easy for you to calculate your daily calorie intake")

list1=[]
list2=[]

meal_amount=int(input("Enter how many meals you had today?"))

#Data input

for i in range(meal_amount):
    meal=input("Enter the meal you ate:")
    calorie=float(input("Enter the amount of calories it contains:"))
    list1.append(meal)
    list2.append(calorie)
print("meals list:",list1)
print("calories list:",list2)

total_Calories=sum(list2)
print(total_Calories)
avg_calories=total_Calories/len(list2)
limit=float(input("Enter the daily calorie limit:"))
if total_Calories > limit:
    print("You have exceeded your calorie goal")
else:
    print("You are within you calorie goal")

#summary table

print("Meal Name\tCalorie")
print("-----------------------")
for i in range(len(list1)):
    print(f"{list1[i]}\t\t{list2[i]}")
print("Total:\t\t",total_Calories)
print("Average:\t",avg_calories)

save=input("Do you want to save the report?")
if save == 'yes':
    with open("calorie.txt","w") as file:
        file.write("Daily Calorie Report\n")
        file.write(f"Date & Time: {datetime.now()}\n\n")
        for i in range(len(list1)):
            file.write(f"{list1[i]} - {list2[i]} calories\n")
        file.write(f"\nTotal calories: {total_Calories}\n")
        file.write(f"Average calories: {avg_calories:.2f}\n")
        if total_Calories > limit:
            status="You have exceeded your calorie goal"
        else:
            status="You are within your calorie goal"
        file.write(f"Status: {status}\n")

            
    print("Report saved successfully")
else:
    print("Report not saved")
        
