
# Task given the gross profit of an individual find the net profit

# Lets begin by allowing the user to input their gross profit to find net profit
try:
    grossprofit = float(input("Let us calculate your net profit, please enter your current gross profit"))
    print("Thank you for entering a feasible number for you grossprofit")
    children = int(input("Please enter the number of children you have"))
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
    print("Thanks for using our services")
finally:
    print("Have a lovely day!")
