





"Program 1"



hoursworked = int(input("Enter hours worked: "))
hourlyrate = int(input("Enter your hourlyrate: "))
print('{} * {} = '.format(hoursworked, hourlyrate))
print("The total is",hoursworked * hourlyrate)

print("Is that what you expected?")
answer = input ("Answer yes or no please: ")
if answer == "yes":
    print("That is a fair amount!")
elif answer == "no":
    print("You still did better than the average!")
else: input("Something went wrong.Would you like to try another calculation? Answer yes or no please: ")
if answer=="no":
    print("Thank you for your time!")
    print("Goodbye!")
    
answer1=input("Would you like to try another calculation? Answer yes or no please: ")
if answer =="yes":
    print("Okay,Let us try it!")
elif answer== "no":
    print("Thank you for your time!")
    print("Goodbye!")
    






"Program 2"




milesdriven=int(input("Enter number of miles driven: "))
gasused=int(input("Enter gas used: "))


print('{} / {} = '.format(milesdriven, gasused))
print("The total is",hoursworked / hourlyrate)

print("On average, you drove this number of miles per galon?")
answer=input("Answer yes or no: ")
if answer == "yes":
    print("That is a good number of miles per one galon!")
elif answer =="no":
    print("Revise your numbers!")
else: input("An error occurred. Would you like to try another calculation? Answer yes or no please: ")
answer2=input("Answer yes or no: ")
if answer == "yes":
    print("Good work! That's impressive.")
    print("Thank you!")
    print("Goodbye!")
    
elif answer=="no":
    print("Thank you for your help!")
    print("Goodbye!")
    
