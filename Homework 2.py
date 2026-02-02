
# Task given the gross profit of an individual find the net profit

# Lets begin by allowing the user to input their gross profit to find net profit
try:
    grossprofit = float(input("Let us calculate your net profit, please enter your current gross profit "))
    print("Thank you for entering a feasible number for you gross profit")
    children = int(input("Please enter the number of children you have "))
    print("Thank you for entering a feasible number of children")

except ValueError:
    # In case someone adds something that is not right I will return
    print("that is not a proper input")
    print("Do not be smart with me")
except NameError:
    print("You are misspelling something")
#    incase of typo
except:
    print("I am sorry, the error is unexpected")
else:
    print("Thank you for using our services")
finally:
    print("Have a lovely day!")

if grossprofit < 1000 and children == 0:
    print("Your gross propfit is ", grossprofit*0.90)
elif 2000 > grossprofit > 1000 and children == 0:
    print("Your gross propfit is ", grossprofit * 0.88)
elif 4000 > grossprofit > 2000 and children == 0:
    print("Your gross propfit is ", grossprofit * 0.86)
elif 2000 > grossprofit > 1000 and children == 0:
    print("Your gross propfit is ", grossprofit * 0.88)
elif 4000 > grossprofit > 2000 and children == 0:
    print("Your gross propfit is ", grossprofit * 0.86)