# functions in python
# first def keyword , then function name, then parameters in parentheses, then colon, 
# then indented block of code

def addNumbers(a, b):
    return a + b  

resultNumbers = addNumbers(5, 10)
print(resultNumbers)

examNumber = [85, 90, 78, 92, 88]

result = sum(examNumber)  # Using the built-in sum() function to calculate the total of the numbers in the list

average = result / len(examNumber)

print(result)  # This will print the total sum of the exam numbers
print(average)  # This will print the average of the exam numbersaverage   


# input from a user 

user_number1 = int(input("Enter First number: "))
user_input2 = int(input("Enter Second number: "))

result = addNumbers(user_number1, user_input2)

print('your addnumber result is ' + str(result))